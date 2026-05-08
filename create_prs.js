const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const mapping = {
  '6811605517369136853': 'anime_list',
  '15816794070085220638': 'high-signal',
  '10237693790487772199': 'CodeVetter',
  '1148218232137194621': 'everythingrated',
  '12303444775638243715': 'free-ai',
  '1744507279859841354': 'open-historia',
  '2699600544811553767': 'clash-royale-meta',
  '1265920242685112073': 'ludo-pass-play',
  '5234227377812329592': 'personalsite',
  '2084116775140528759': 'starboard',
  '13774030315237897132': 'swe-interview-prep',
  '6098476140172166721': 'truehire',
  '17417799823148245681': 'looptv',
  '8997991944747528983': 'saas-maker',
  '12466352283700906749': 'chess',
  '17556014885814734494': 'significanthobbies',
  '13996138630673391089': 'reader',
  '3438151884847403724': 'agentMode',
  '9826406226774156063': 'resume-tailor',
  '15133698087945827733': 'mentionpilot',
  '9185309910565444470': 'linkchat',
  '11314275126436624268': 'today-little-log',
  '15554881489758316303': 'backpropagate',
  '1467829767334424076': 'email-manager'
};

const outputDir = '/Users/sarthakagrawal/.gemini/tmp/saas-ideas/tool-outputs/session-9524441b-cfb9-49e1-ac86-0907cfb572d5/';
const fleetDir = path.resolve(__dirname, '../../fleet');

const projectUrls = {};

// Parse all tool output files to extract download URLs
const files = fs.readdirSync(outputDir);
for (const file of files) {
  if (file.startsWith('mcp_stitch_generate_screen_from_text') || file.startsWith('mcp_stitch_get_screen')) {
    const content = fs.readFileSync(path.join(outputDir, file), 'utf-8');
    try {
      // Find JSON strings and extract
      // Since the output is sometimes wrapped in <tool_output_masked> or Output:, we can use regex
      const jsonStrMatch = content.match(/\{.*\}/s);
      if (jsonStrMatch) {
         let data = JSON.parse(jsonStrMatch[0]);
         if (data.output) {
             data = JSON.parse(data.output);
         }
         let projId = data.projectId;
         if (!projId && data.name) {
             const m = data.name.match(/projects\/(\d+)/);
             if (m) projId = m[1];
         }
         
         if (projId && data.outputComponents) {
            for (const comp of data.outputComponents) {
               if (comp.design && comp.design.screens) {
                   for (const screen of comp.design.screens) {
                       if (screen.htmlCode && screen.htmlCode.downloadUrl) {
                           projectUrls[projId] = screen.htmlCode.downloadUrl;
                       }
                   }
               }
            }
         } else if (projId && data.screenshot && data.htmlCode) {
             projectUrls[projId] = data.htmlCode.downloadUrl;
         }
      }
    } catch (e) {
       // Ignore parse errors for individual files
    }
  }
}

// Fallback regex approach if JSON parsing failed due to truncation in some files
for (const file of files) {
    if (file.startsWith('mcp_stitch_generate_screen_from_text') || file.startsWith('mcp_stitch_get_screen')) {
        const content = fs.readFileSync(path.join(outputDir, file), 'utf-8');
        const projMatch = content.match(/"projectId":"(\d+)"/);
        const urlMatch = content.match(/"htmlCode":\{"name":"[^"]*","downloadUrl":"([^"]+)"/);
        
        let projId = projMatch ? projMatch[1] : null;
        if (!projId) {
             const m = content.match(/"name":"projects\/(\d+)\/screens\//);
             if (m) projId = m[1];
        }
        
        if (projId && urlMatch && !projectUrls[projId]) {
             projectUrls[projId] = urlMatch[1];
        }
    }
}

async function processProjects() {
    let successCount = 0;
    for (const [projId, folder] of Object.entries(mapping)) {
        console.log(`\nProcessing ${folder} (Project ID: ${projId})...`);
        const url = projectUrls[projId];
        if (!url) {
            console.log(`⚠️  No download URL found for ${folder}. Skipping.`);
            continue;
        }
        
        const targetDir = path.join(fleetDir, folder);
        if (!fs.existsSync(targetDir)) {
             console.log(`⚠️  Directory ${targetDir} does not exist. Skipping.`);
             continue;
        }

        try {
            console.log(`Downloading HTML...`);
            const res = await fetch(url);
            const html = await res.text();
            
            // Write to a design.html file in the root of the project
            const htmlPath = path.join(targetDir, 'design.html');
            fs.writeFileSync(htmlPath, html);
            
            console.log(`Running git commands...`);
            const branchName = `design-revamp-${Date.now()}`;
            
            execSync(`git checkout -b ${branchName}`, { cwd: targetDir, stdio: 'ignore' });
            execSync(`git add design.html`, { cwd: targetDir, stdio: 'ignore' });
            execSync(`git commit -m "feat: apply Stitch design revamp"`, { cwd: targetDir, stdio: 'ignore' });
            execSync(`git push -u origin ${branchName}`, { cwd: targetDir, stdio: 'ignore' });
            
            console.log(`Creating PR...`);
            execSync(`gh pr create --title "feat: apply Stitch design revamp" --body "Automated PR to apply the new design generated by Stitch."`, { cwd: targetDir, stdio: 'ignore' });
            
            console.log(`✅ Successfully raised PR for ${folder}`);
            successCount++;
        } catch (e) {
            console.log(`❌ Failed to process ${folder}: ${e.message}`);
        }
    }
    console.log(`\nFinished processing! Successfully raised PRs for ${successCount} projects.`);
}

processProjects();
