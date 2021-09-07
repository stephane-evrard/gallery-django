$(function() {
    $("input").click(function() {
    $(this).focus();
    $(this).select();
    document.execCommand('copy');
    $(this).after("Copied to clipboard");
    });
   });


   // init Masonry
var $grid = $('.grid').masonry({
    itemSelector: '.grid-item',
    percentPosition: true,
    columnWidth: '.grid-sizer'
  });
  
  // layout Masonry after each image loads
  $grid.imagesLoaded().progress( function() {
    $grid.masonry();
  });