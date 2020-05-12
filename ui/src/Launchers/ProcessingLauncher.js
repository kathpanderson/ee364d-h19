import React from 'react';
import { SectionTitle, CustomButton } from '../lib.js';

class ProcessingLauncher extends React.Component {
  render() {
    return (
        <div class="tile is-vertical is-bordered-bottom is-parent">
          <SectionTitle title="Process Data"/>
          {this.fileSelector()}
          <CustomButton name="Start Processing"/>
          <div class="tile is-parent is-custom-tile is-hidden">
            Progress bar
          </div>
        </div>
    );
  }

  fileSelector() {
    return (
      <div class="tile is-parent is-custom-tile">
        <div class="tile is-child checkbox-label is-2">Data File:</div>
        <div class="tile field is-marginless is-child">
          <div class="control">
            <textarea
              class="textarea has-fixed-size"
              rows="1"
              placeholder="custom/file/path/here"
            />
          </div>
        </div>
      </div>
    )
  }
}



export default ProcessingLauncher;
