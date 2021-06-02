function clicked(a) {
  var b = a.firstElementChild.innerHTML;
  var word = '';
  for (i=0;i<b.length;i++) {
    if (b[i] == ' ') {
      continue;
    }
    else if (b[i] == '\n') {
      continue;
    }
    else {
      word += b[i];
    }
  }
  answer = '';
  b = document.getElementById("answer").innerText;
  for (i=0;i<b.length;i++) {
    if (b[i] == ' ') {
      continue;
    }
    else if (b[i] == '\n') {
      continue;
    }
    else {
      answer += b[i];
    }
  }
  if (word == answer) {
    window.location.href = "http://127.0.0.1:5000/correct";
  }
  else {
    window.location.href = "http://127.0.0.1:5000/wrong";
  }
}

function correct() {
  setTimeout(function() {window.location.href = 'http://127.0.0.1:5000/';}, 2000);
}

function wrong() {
  window.location.href = 'http://127.0.0.1:5000/';
}
