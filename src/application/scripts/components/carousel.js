const Carousel = ( () => {
  var carouselElements = document.querySelectorAll( '.carousel' );
  [].forEach.call( carouselElements, function( el )
  {
    var items = el.querySelector( '.carousel-items' );
    var itemCount = items.querySelectorAll( '.carousel-item' ).length;
    var currentIndex = 0;

    items.style.left = '0%';

    function onUpdate()
    {
      currentIndex = ( currentIndex < 0 ) ? itemCount - 1 : currentIndex;
      currentIndex = ( currentIndex >= itemCount ) ? 0 : currentIndex;
      items.style.left = ( -100 * currentIndex ) + '%';
    }

    el.querySelector( '.carousel-controls .left' ).addEventListener( 'click', function( e ){
      currentIndex -= 1;
      onUpdate();
    } );

    el.querySelector( '.carousel-controls .right' ).addEventListener( 'click', function( e ){
      currentIndex += 1;
      onUpdate();
    } );
  });
} )();
export default Carousel;
