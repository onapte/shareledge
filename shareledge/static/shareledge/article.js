function hide(element) {
    element.style.display = "none";
}

function show(element) {
    element.style.display = "block";
}

function editArticle(articleId) {
    //window.location.href = `/articles/${articleId}`;
    fetch(`/edit/${articleId}`, {
        method:'post',
        body: {id:'articleId'}
        // headers : { 
        //     'Content-Type': 'application/json',
        //     'Accept': 'application/json'
        //    }
    })
    .then(response => response.json())
    .then(data => {
        let d = JSON.stringify(data);
        console.log(d);
    })
    
};

function saveEdits(articleId) {
    const xhr = new XMLHttpRequest();
    
    alert(1);
    xhr.onreadystatechange = function () {
        if (xhr.status === 200) {

            // Changing string data into JSON Object
            obj = JSON.parse(xhr.responseText);
            console.log(obj);
        }
    }
    xhr.open("POST", `/articles/edit/${articleId}`, true);
    xhr.send();
}


function starColour(starName) {
    if (starName === "s1") {
        document.querySelector('#s1').style.color = "orange"; 
    }
    if (starName === "s2") {
        document.querySelector('#s2').style.color = "orange";
        document.querySelector('#s1').style.color = "orange"; 
    }
    if (starName === "s3") {
        document.querySelector('#s3').style.color = "orange";
        document.querySelector('#s2').style.color = "orange";
        document.querySelector('#s1').style.color = "orange";
    }
    if (starName === "s4") {
        document.querySelector('#s4').style.color = "orange";
        document.querySelector('#s3').style.color = "orange";
        document.querySelector('#s2').style.color = "orange";
        document.querySelector('#s1').style.color = "orange";
    }
    if (starName === "s5") {
        document.querySelector('#s5').style.color = "orange";
        document.querySelector('#s4').style.color = "orange";
        document.querySelector('#s3').style.color = "orange";
        document.querySelector('#s2').style.color = "orange";
        document.querySelector('#s1').style.color = "orange";
    }
}

function uncolour(starName) {
    if (starName === "s1") {
        document.querySelector('#s1').style.color = "black"; 
    }
    if (starName === "s2") {
        document.querySelector('#s2').style.color = "black";
        document.querySelector('#s1').style.color = "black";
    }
    if (starName === "s3") {
        document.querySelector('#s3').style.color = "black";
        document.querySelector('#s2').style.color = "black";
        document.querySelector('#s1').style.color = "black";
    }
    if (starName === "s4") {
        document.querySelector('#s4').style.color = "black";
        document.querySelector('#s3').style.color = "black";
        document.querySelector('#s2').style.color = "black";
        document.querySelector('#s1').style.color = "black";
    }
    if (starName === "s5") {
        document.querySelector('#s5').style.color = "black";
        document.querySelector('#s4').style.color = "black";
        document.querySelector('#s3').style.color = "black";
        document.querySelector('#s2').style.color = "black";
        document.querySelector('#s1').style.color = "black";
    }
}

document.addEventListener('DOMContentLoaded', function() {
    // document.querySelector('#edit-button').onclick = function() {
    //     let contentDiv = document.querySelector('#main-content');
    //     contentDiv.setAttribute("contentEditable", true);
    //     hide(document.querySelector('#edit-button'));
    //     show(document.querySelector('#saveChanges-button'));
    //     show(document.querySelector('#cancel-button'));
    // };
    
    document.querySelector('#comment-submit').onclick = function() {
        document.querySelector('#comment-data').value = document.querySelector('#comment').innerHTML;
        
    }
    document.querySelector('#s1').onmouseenter = function() {
        starColour("s1");
    };
    document.querySelector('#s1').onmouseleave = function() {
        uncolour("s1");
    };
    document.querySelector('#s2').onmouseenter = function() {
        starColour("s2");
    };
    document.querySelector('#s2').onmouseleave = function() {
        uncolour("s2");
    };
    document.querySelector('#s3').onmouseenter = function() {
        starColour("s3");
    };
    document.querySelector('#s3').onmouseleave = function() {
        uncolour("s3");
    };document.querySelector('#s4').onmouseenter = function() {
        starColour("s4");
    };
    document.querySelector('#s4').onmouseleave = function() {
        uncolour("s4");
    };document.querySelector('#s5').onmouseenter = function() {
        starColour("s5");
    };
    document.querySelector('#s5').onmouseleave = function() {
        uncolour("s5");
    };
    // document.querySelectorAll('.fa-star').forEach(star => {
    //     star.onclick = function() {
    //         let starName = star.getAttribute('name');
    //         starColour(starName);
    //         hide(document.querySelector('#rating-section'));
    //         show(document.querySelector('#thanks-for-rating'));
    //     }
    // })
    document.querySelector('#get-pdf').onclick = function() {
        document.querySelector('#pdf-content').value = document.querySelector('#article-section').innerHTML;
    }
    
    hide(document.querySelector('#thanks-for-rating'));
});