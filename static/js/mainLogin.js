const inputs = document.querySelectorAll(".input");
var btn = document.getElementById("btn");

function addcl(){
	let parent = this.parentNode.parentNode;
	parent.classList.add("focus");
	console.log("remove")
}

btn.addEventListener("click", function(e){
	
})


function remcl(){
	let parent = this.parentNode.parentNode;
	if(this.value == ""){
		parent.classList.remove("focus");
		console.log("add")
	}
}


inputs.forEach(input => {
	input.addEventListener("focus", addcl);
	input.addEventListener("blur", remcl);
});
