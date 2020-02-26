import React from 'react';

class TestLauncher extends React.Component {
  render() {
    return (
        <div class="tile is-vertical is-bordered-bottom">
          {this.filepathOptions()}
          {this.visualizerOptions()}
            {this.startButton()}
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

  startButton() {
    return (
      <div class="tile is-parent is-custom-tile">
        <div class="tile is-child">
          <button>Start Test</button>
        </div>
      </div>
    )
  }
}

export default TestLauncher;
