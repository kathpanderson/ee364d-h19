import React from 'react';
import {
  SectionTitle,
  CustomButton,
  getHardwareArgsStr,
  getProcessingArgsStr
} from '../lib.js';

class TestLauncher extends React.Component {
  render() {
    return (
        <div class="tile is-parent is-vertical is-bordered-bottom">
          <SectionTitle title="Run Test"/>
          {this.filepathOptions()}
          {this.visualizerOptions()}
          <CustomButton name="Start Test" onClickEvent={this.launchTest}/>
          <div class="tile is-parent is-custom-tile is-hidden">
            Progress bar
          </div>
        </div>
    );
  }

  filepathOptions() {
    return (
      <div class="tile is-parent is-custom-tile">
        <div class="tile is-child checkbox-container is-1">
         <label><input type="checkbox" class="checkbox is-custom-checkbox"/></label>
        </div>
        <div class="tile is-child checkbox-label is-3">Custom File Path:</div>
        <div class="tile field is-marginless is-child">
          <div class="control">
            <textarea
              class="textarea has-fixed-size"
              rows="1"
              placeholder="custom/file/path/here"
            />
          </div>
        </div>
        <div class="tile is-child checkbox-container is-1"/>
      </div>
    )
  }

  visualizerOptions() {
    return (
      <div class="tile is-parent is-custom-tile">
        <div class="tile is-child checkbox-container is-1">
         <label><input type="checkbox" class="checkbox is-custom-checkbox"/></label>
        </div>
        <div class="tile is-child option-unit has-text-left">Launch Visualizer on Completion</div>
        <div class="tile is-child checkbox-container is-1"/>
      </div>
    )
  }

  launchTest() {
    var hardwareArgs = getHardwareArgsStr();
    var processingArgs = getProcessingArgsStr();
  }
}

export default TestLauncher;
