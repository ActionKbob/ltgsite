const Collapse = ( () => {
  var collapseElements = document.querySelectorAll( '.collapse' );
  [].forEach.call( collapseElements, function( el )
  {
    el.querySelector( '.collapse-toggle' ).addEventListener( 'click', function( e ){
      el.querySelector( '.collapse-content' ).classList.toggle( 'shown' );
    } );
  });
} )();
export default Collapse;
