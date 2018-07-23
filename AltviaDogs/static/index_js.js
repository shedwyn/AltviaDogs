// js specific to index Page
'use strict';
//inputs

function checkForBlankValue(aValue){
  if (aValue !== "") {
    return false
  }
  else {
    return true
  }
}

//transform

//create

function rejectWithMessage(){

}

//mains


function correctDateEntry(aValue){
  if (checkForBlankValue(aValue) === false){
    rejectWithMessage
  }
  else {
    formatDateForPost(aValue)
  }
}

//registration


document.getElementById('date-choice-form').addEventListener('submit', function(){
  let dateChoice = document.getElementById('date_choice').value
  correctDateEntry(dateChoice)
})
