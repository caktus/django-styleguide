var toggle = function(el){
	if (el.classList.contains('open')){
		el.classList.remove('open')
	}else{
		el.classList.add('open')
	}
}

// toggle sub_menus
var toggleMenus = document.getElementsByClassName('toggle-menu')
Array.prototype.forEach.call(toggleMenus, function(el) {
	el.onclick = function(){
        if(this.nextElementSibling.querySelectorAll('.selected').length == 0){
            toggle(this)
        }
	}
})

var hamburger = document.getElementById('hamburger')
hamburger.onclick = function(event){

	//toggle button image
	var src = this.children[0].src,
		src_array = src.split('/')
		src_type = src_array[src_array.length - 1].split('.')[0]

	if (src_type == 'hamburger'){
		this.children[0].src = src.replace('hamburger', 'close')
	}else{
		this.children[0].src = src.replace('close', 'hamburger')
	}

	// toggle nav
	var nav = document.getElementById('styleguide-menu')
	toggle(nav)
}

