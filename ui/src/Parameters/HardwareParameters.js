import React from 'react';
import { SectionTitle } from '../lib.js';

function HardwareParameters() {
  // TODO: Add warnings, way to enable/disable preamp
  return (
    <div class="tile is-vertical is-bordered-bottom is-parent">
      <SectionTitle title="Hardware Parameters"/>
      <div class="tile is-vertical">
      <div class="tile subsection-title is-italic">Pre Amp</div>
        <div class="tile is-parent is-custom-tile">
          <div class="tile is-child option-label">
            Enabled:
          </div>
          <div class="tile is-child option-unit">
            <label>
              <input
                type="checkbox"
                class="checkbox is-custom-checkbox"
                id="preampEnabledVal"
              />
            </label>
          </div>
        </div>
        <div class="tile is-parent is-custom-tile">
          <div class="tile is-child option-label">
            Input Current Range:
          </div>
          <div class="tile is-child">
            {gainDropDown()}
          </div>
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
          <select id="preampVal">
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
