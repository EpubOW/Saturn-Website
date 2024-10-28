document.getElementById( "right-button" ).onclick = () => {
    item = document.getElementById( "carusel" )
    item.scroll({
        left: item.scrollLeft + 342,
        top: 0,
        behavior: 'smooth'
    })
    
}

document.getElementById( "left-button" ).onclick = () => {

    item = document.getElementById( "carusel" )
    item.scroll({
        left: item.scrollLeft - 342,
        top: 0,
        behavior: 'smooth'
    })

}