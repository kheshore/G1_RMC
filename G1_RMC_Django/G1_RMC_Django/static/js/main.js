console.log("1111",1111);

// delete button in orders page
$(document).ready(function(){
    $(".delete-btn").click(function(e){
      console.log("Delete button clicked");
      if (!confirm('Are you sure you want to delete this order?')) {
        e.preventDefault();
      }
    });
});
