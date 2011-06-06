var comics;
$(function() {
  $.get('/static/files/comic.list', function(data) {
    comics = data.split("\n"); clickComic();
  });
});
function clickComic() {
  $("#comic").unbind().fadeOut('fast', function() {
    $("#comic").attr({src: '/static/images/load.gif', title: 'loading'}).fadeIn();
    var comic = comics[Math.floor(Math.random()*comics.length)];
    $(document.createElement("img")).attr('src', comic).load(function() {
      $("#comic").hide().attr({src: comic, title: 'Giantitp comics'}).fadeIn().click(clickComic);
    });
  });
}
