import React from 'react';
// import { exec } from 'child_process';

class SectionTitle extends React.Component {
  render() {
    return (
      <div class="tile is-custom-tile is-parent has-text-weight-bold">
        <div class="tile is-child">{this.props.title}</div>
      </div>
    );
  }
}

class CustomButton extends React.Component {
  render() {
    return (
      <div class="tile is-parent is-custom-tile">
        <div class="tile is-child">
          <button onClick={this.props.onClickEvent}>{this.props.name}</button>
        </div>
      </div>
    )
  }
}

// Used to control order params appear in processing args string
// All are the IDs of the elems that contain this information
// EXCEPT for daqSampling. daqSampling is the root for the two
// elems that contain DAQ sampling rate info; append "Unit"
// and "Val" to this root to get the two data fields.
const processingArgs = [
  "photo1Val",
  "photo2Val",
  "tipCurrentVal",
  "tipBiasVal",
  "imageXVal",
  "imageYVal",
  "daqSampling" 
];

// Dict to map a unit in the DAQ sampling unit drop down to a
// correct value multiplier
const hzToMultiplier = {
  "Hz": 1,
  "kHz": 1000,
  "MHz": 1000000,
  "GHz": 1000000000
};

// TODO: use this function to ensure params read in get***ArgsStr
// functions below are correct format.
function isNumber(num) {
  return num.match(/^\d+$/) || num.match(/^\d+\.\d+$/);

}

function getProcessingArgsStr() {
  var args = "";
  var e;

  processingArgs.forEach(function (arg){
    if (arg === "daqSampling") {  // DAQ params are special case
      e = document.getElementById(arg + "Unit");
      var multiplier = hzToMultiplier[e.options[e.selectedIndex].value];
      
      e = document.getElementById(arg + "Val");
      var val = e.value * multiplier;
      args = args + val + " "
    }
    else {
      // Extract value and append to arg string
      e = document.getElementById(arg);
      args = args + e.value + " ";
    }
  });

  return args;
}

function getHardwareArgsStr() {
  var args = [];

  var e = document.getElementById("preampVal");
  args.push(e.options[e.selectedIndex].value);

  e = document.getElementById("preampEnabledVal");
  args.push(e.checked);

  return args;
}

var exec = require('child_process').execFile;
/**
 * Function to execute exe
 * @param {string} fileName The name of the executable file to run.
 * @param {string[]} params List of string arguments.
 * @param {string} path Current working directory of the child process.
 */
function execute(fileName, params, path) {
    let promise = new Promise((resolve, reject) => {
        exec(fileName, params, { cwd: path }, (err, data) => {
            if (err) reject(err);
            else resolve(data);
        });

    });
    return promise;
}

function launchLabview() {
  var executablePath = "C://Users//katie//Downloads//Application.exe";

  const proc = require('child_process');
  const p = execute(executablePath, [], "");

  // p.on('close', code => {
  //   console.log("child process exited with code " + code);
  // });
}

export { 
  SectionTitle,
  CustomButton,
  getProcessingArgsStr,
  getHardwareArgsStr,
  launchLabview
}