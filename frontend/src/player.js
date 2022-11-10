import React from 'react';
import audio1 from './/audio1.mp3';

function Player() {

  function play() {
    switchPlay = true
    var audio = document.getElementById("audio");
    audio.play();
    console.log("on click working")
  }
  
  return (
    <div>
        <button id="botao" onClick={play}>
        why not
        </button> 
        <div id="mediaPlaya">
        <audio id="audio" controls>
        <source src={audio1} type="audio/ogg" />
        Your browser does not support the audio tag.
        </audio>
        </div>
    </div>
  );
}

export default Player;
