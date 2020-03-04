import React from 'react';

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

const processingArgs = [
  "photo1Val",
  "photo2Val",
  "tipCurrentVal",
  "tipBiasVal",
  "imageXVal",
  "imageYVal",
  "daqSampling"
];

const hzToMultiplier = {
  "Hz": 1,
  "kHz": 1000,
  "MHz": 1000000,
  "GHz": 1000000000
};

function getProcessingArgsStr() {
  var args = "";
  var e;

  processingArgs.forEach(function (arg){
    if (arg === "daqSampling") {
      e = document.getElementById(arg + "Unit");
      var multiplier = hzToMultiplier[e.options[e.selectedIndex].value];
      
      e = document.getElementById(arg + "Val");
      var val = e.value * multiplier;
      args = args + val + " "
    }
    else {
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

export { 
  SectionTitle,
  CustomButton,
  getProcessingArgsStr,
  getHardwareArgsStr
}