// biến chứa hình ảnh lớn
var largeImage = document.querySelector('.large-image img')

// danh sách chứa các hình ảnh nhỏ
var smallImageList = document.querySelectorAll('.small-image div')

// biến chứa chỉ số index hiện tại
var currentIndex = 0

setCurrentIndex(currentIndex)

// Xây dựng hàm lấy chỉ số index của hình ảnh nhỏ được chọn
function setCurrentIndex(index) {
  currentIndex = index
  largeImage.src = smallImageList[currentIndex].querySelector('img').src
}

// Xây dựng hàm xử lý sự kiện khi click vào từng hình nhỏ bên dưới
smallImageList.forEach((img, index) => {
  img.addEventListener('click', () => {
    setCurrentIndex(index)
  })
})

// Cho hình ảnh thay đổi sau khoảng 3 giây
setInterval(function (){
  currentIndex++
  if (currentIndex >= smallImageList.length) {
    currentIndex = 0
  }
  setCurrentIndex(currentIndex)
}, 3000)