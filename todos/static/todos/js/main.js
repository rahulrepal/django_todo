
todos = document.getElementById("todos")

for(children of todos.children){
    children.addEventListener("focus",function(e){
        this.classList.add("active")

    })
        children.addEventListener("blur",function(e){
        this.classList.remove("active")

    })
}