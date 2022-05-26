'use strict'

let picks = []
let csrf = $('input[name=csrfmiddlewaretoken]').val()

$('.vote-button').click(vote_tally)
$('#submit-votes').click(submit_votes)

function vote_tally(e) {
  console.log("asdasd")
  console.log(e.target.value)
  console.log(picks)

  if (!picks.includes(e.target.value)) {
    picks.push(e.target.value)
  }
}

function submit_votes() {
  localStorage.setItem('picks', picks)
  console.log(picks)

  $.ajax({
    type: 'POST',
    url: '/results/',
    data: {
      picks: picks,
      csrfmiddlewaretoken: csrf,
    },
    success: function() {
      location = '/results' // redirect to results page
    }
  })
} 