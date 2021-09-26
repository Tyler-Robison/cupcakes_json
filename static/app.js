async function getCupcakes() {
    const cupcakeList = document.querySelector('#cupcake-list');
    cupcakeList.innerHTML = ''
    const res = await axios.get('/api/cupcakes');
    const cupcakes = res.data.cupcakes;

    for (let cupcake of cupcakes) {
        const li = document.createElement('li');
        const flavorPara = document.createElement('p');
        const sizePara = document.createElement('p');
        const ratingPara = document.createElement('p');
        const imagePara = document.createElement('p');
        flavorPara.innerText = `${cupcake.flavor}`;
        sizePara.innerText = `${cupcake.size}`;
        ratingPara.innerText = `${cupcake.rating}`;
        imagePara.innerText = `${cupcake.image}`;
        li.append(flavorPara);
        li.append(sizePara);
        li.append(ratingPara);
        li.append(imagePara);
        cupcakeList.append(li);
    }
}

getCupcakes();

document.querySelector('#cupcake-button').addEventListener('click', createCupcake);

async function createCupcake(e) {
    e.preventDefault();
    const flavor = document.querySelector('#flavor').value
    const size = document.querySelector('#size').value
    const rating = document.querySelector('#rating').value
    const image = document.querySelector('#image').value
    const res = await axios.post('/api/cupcakes', data = {
        'flavor': flavor,
        'size': size,
        'rating':rating,
        'image': image
    });

    getCupcakes()
    document.querySelector('#flavor').value = ''
    document.querySelector('#size').value = ''
    document.querySelector('#rating').value = ''
    document.querySelector('#image').value = ''
}

// $('.delete-todo').click(deleteTodo)

// async function deleteTodo(){
//   const id = $(this).data('id')
//   res = await axios.delete(`/api/todos/${id}`)
//   $(this).parent().remove()
// }