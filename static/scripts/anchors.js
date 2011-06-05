$(function() {
    $("h2").each(function(idx) {
        $(this).append( $(document.createElement("a"))
            .attr({class:'anchor', href:'#'+this.getAttribute('id')}).text("\u00B6"));
    });
});
