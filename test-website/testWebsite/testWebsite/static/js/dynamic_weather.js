function getRandomArbitrary(min, max) {
  return Math.random() * (max - min) + min;
}


setInterval(function() {
  $("#unit").text(Math.ceil(getRandomArbitrary(-40, 49)));
}, 5000);
