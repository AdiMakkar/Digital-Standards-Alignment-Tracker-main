// Import the required npm packages
const fs = require("fs");
const lighthouse = require("lighthouse");
const chromeLauncher = require("chrome-launcher");
  
// Read the csv file and store the
// urls in an array
var array = fs.readFileSync("URLs.csv")
                .toString().split("\n");
  
// Declare a resultant array to store 
// the generated scores and initialize
// it with headings
let result = [];
result.push(
  ", URL, Mobile_Accessibility, Desktop_Accessibility"
);
  
// The async await is used to ensure 
// non-blocking code execution 
(async () => {
  const chrome = await chromeLauncher
    .launch({ chromeFlags: ["--headless"] })
  
  // Declaring an object to specify score 
  // for what audits, categories and type
  // of output that needs to be generated 
  const options = {
    logLevel: "info",
    output: "csv",
    onlyCategories: ["accessibility"],
    audits: [
      "first-meaningful-paint",
      "first-cpu-idle",
      "byte-efficiency/uses-optimized-images",
    ],
    port: chrome.port,
  };
  
  // Traversing through each URL 
  for (i in array) {
  
    // Separate strategy for Mobile
    // and Desktop view
    for (let x = 0; x < 2; x++) {
      let configuration = "";
  
      if (x == 0) options.strategy = "mobile";
      else options.strategy = "desktop";
  
      const runnerResult = 
        await lighthouse(`https://${array[i]}`, options);  
  
      // Current report
      const reportCsv = runnerResult.report;
  
      // URL to be put only for first iteration 
      // (mobile and not separately for desktop)
      if (x == 0) {
        result.push("\n");
        result.push(runnerResult.lhr.finalUrl);
      }
  
      // If score can't be determined, NA is 
      // put in the corresponding field.   
      if (runnerResult.lhr.categories.accessibility.score) {
        result.push(runnerResult.lhr
              .categories.accessibility.score * 100)
      } else {
        result.push(" ");
      }
    }
  }
  
  // Append the result in a report.csv 
  // file and end the program
  fs.appendFileSync("results.csv", result.toString());
  await chrome.kill();
})();