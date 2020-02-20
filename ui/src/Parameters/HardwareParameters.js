import React from 'react';

function HardwareParameters() {
  return (
    <div class="tile is-vertical">
      <div class="tile has-text-weight-bold">Hardware Parameters</div>
      <div class="tile is-parent is-custom-tile">
        <div className="tile is-child option-label">
          Amp Order of Magnitude:
        </div>
        <div className="tile is-child">
          {gainDropDown()}
        </div>
      </div>
    </div>
  );
}

function gainDropDown() {
  return (
    <div class="field">
      <div class="control">
        <div class="select">
          <select>
            {generateGainOptions()}
          </select>
        </div>
      </div>
    </div>
  )
}

function generateGainOptions() {
  var optionsToProvide = [
    "1mA", "100uA", "10uA", "1uA",
    "100nA", "10nA", "1nA", "100pA", "10pA"
  ];

  var options = [];
  optionsToProvide.forEach(function(option) {
    options.push(<option value={option}>{option}</option>);
  });

  return options;
}

export default HardwareParameters;
