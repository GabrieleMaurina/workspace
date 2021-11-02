function check(){
	console.log('checking')
	let div = document.getElementById('deadManButton')
	if (div && div.style.display === 'block'){
		console.log('found')
		div.click()
	}
	let li = document.getElementsByClassName('current')
	if (li && li[0] && li[0].firstChild && li[0].firstChild.firstChild){
		console.log('opening new class')
		li[0].firstChild.firstChild.click()
	}
	setTimeout(check,1000)
}
check()