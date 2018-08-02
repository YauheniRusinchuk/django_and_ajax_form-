$(function(){

  $(".form").on('submit', (e) => {
    e.preventDefault();
    create_comment()
  })

});


function create_comment() {
  $.ajax({
    url: $(this).attr('action'),
    type: 'POST',
    data: {
      comment: $('.text_comment_form').val(),
      csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
    },
    success : function(data) {
      let newItem = document.createElement('p')
      newItem.innerHTML = data.message;
      $('.div_todo').prepend(newItem);
    }
  })
}
