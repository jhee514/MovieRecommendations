# README

## Project04 | 20190809

  Project 04에서는 HTML 을 통한 웹 페이지 마크업, CSS 를 통한 선택자 활용 및 웹 페이지 꾸미기, Bootstrap을 활용한 HTML/CSS, JS 라이브러리 활용 및 영화 추천 사이트 반응형 레이아웃 구성을 하는 것이 목표이다.



### 01_layout 

  영화 추천 사이트 메인 페이지 기초 레이아웃을 구성합니다.

1. Navigation Bar

   ```html
   <nav class="navbar navbar-light navbar-expand-lg fixed-top" style="color: black; background-color: white">
       <a class="navbar-brand" href="#">MOVIE NIGHT</a>
       <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
         aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
         <span class="navbar-toggler-icon"></span>
       </button>
       <div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
         <ul class="navbar-nav">
           <li class="nav-item active">
             <a class="nav-link" href="#">Home<span class="sr-only">(current)</span></a>
           </li>
           <li class="nav-item">
             <a class="nav-link" href="#">Ratings and Reviews</a>
           </li>
           <li class="nav-item">
             <a class="nav-link" href="#">Sigh In</a>
           </li>
         </ul>
       </div>
     </nav>
   ```

   ```css
   nav {
     font-family: 'Poiret One', cursive;
     top: 0;
   }
   ```

   

   - Navigation bar 를 최상단에 위치시키기 위해 nav 의 class 에 'fixed-top' 값을 설정 해주었다. 
   - Item List를 우측 정렬하기 위해 nav > div 의 class 에 'justify-content-end' 값을 설정 해주었다.
   - 반응형으로 구성되어 일정 수준 이하에서는 item이 숨김 처리 될 수 있도록 navbar-expand-lg 값을 nav class에 설정하였다.

   

2. Header

   ```html
     <header>
       <h2>MOVIE NIGHT</h2>
     </header>
   ```

   ```css
   header {
     position: relative;
     width: 100%;
     height: 350px;
     padding: 40px;
     margin-bottom: 10px;
     clear: left;
     background-image: url(images/header.jpg);
     background-size: 100%;
     font-family: 'Poiret One', cursive;
   }
   
   h2 {
     text-align: center;
     line-height: 350px;
   }
   ```

   - 높이는 350px , 너비는 브라우저 전체 영역으로 설정하기 위해 01_layout.css 파일에서 height 값을 350px, width 100% 로 설정하였다.
   - 배경 이미지는 같은 폴더 내 images 폴더에 위치한 header.jpg 를 사용하였다.
   - h2 태그를 Header 영역의 수평 가운데 정렬 시키기 위해 text-align 값은 center, 수직 가운데 정렬을 위해 line-height은 header 의 height 와 같은 350px 로 설정하였다.

3. Footer

   ```html
     <footer class="fixed-bottom">
       Ji Hee
       <a href="#">top</a>
     </footer>
   ```

   ```css
   footer {
     width: 100%;
     height: 50px;
     padding-left: 3rem;
     padding-right: 3rem;
     line-height: 50px;
     font-size: 1rem;
     background-color: white;
     color: black;
     font-family: 'Poiret One', cursive;
   }
   
   footer > a {
     color: black;
     float: right;
   }
   
   a:hover {
     color: coral;
     text-decoration-line: none;
   }
   ```

   - 브라우저 최하단에 위치 시키기 위해 footer 요소 class 에 fixed-bottom 값을 설정해 주었다. 
   - 높이는 50px, 너비는 브라우저 전체 영역으로 설정하기 위해 css 파일에서 footer style을 height 50px, width 100%로 설정하였다. 또한, padding이 좌우로 3rem이 되도록 padding-left, padding-right 값을 3rem으로 설정하였다.
   - 왼쪽에는 이름이 들어가고, 오른쪽에는 헤더로 올라가는 링크로 구성 되도록 각각 텍스트를 작성 후, 헤더로 올라가는 텍스트 'top' 에 ``<a>`` 태그를 이용하여 링크를 걸어 주었다.



### 02_movie

영화 추천 사이트를 위한 영화 리스트 구성(2)

영화 목록 섹션 레이아웃을 만들어 봅시다.

1.  레이아웃

   영화 리스트는 container에 속합니다.

2. (필수) subtitle

   subtitle 영역은 위 아래 margin이 3rem입니다.

   글씨 부분은 h3 태그입니다.

   밑줄은 너비가 70px이고, 색상은 자유롭게 해주세요.

3. Card view

   카드 총 6개 이상이며, 반응형으로 배치해야 합니다.

   한 줄에 보이는 카드의 갯수는 다음과 같이 구성됩니다.

   576px 미만 : 1개

   576px 이상 768px 미만 : 2개

   768px 이상 992px 미만 : 3개

   992px 이상 : 4개

   카드는 각각 위 아래 margin이 1rem입니다.

   이미지는 제공된 이미지를 활용 해주세요.

   이미지는 반드시 alt 속성에 값이 있어야 합니다.

   img의 alt 속성은 alternate의 약자로, 이미지의 대안을 나타냅니다. 이미지가 서버 혹은 경로 오류로 인해 읽어 오지 못할 경우 해당 속성값이 대체하여 나타납니다.

   이미지 밑에는 h4 태그를 활용하여 영화 제목을 작성 해주세요.

   영화 제목 옆에는 네이버 영화 평점을 작성 해주세요.

   영화 평점은 9점 이상인 경우 청색 계열의 색으로, 9점 미만인 경우는 어두운 계열의 색으로 꾸며 주세요.

   제목 및 평점과 내용에는 구분선이 있습니다.

   구분선 아래에는 영화 장르와 개봉일을 작성 해주세요.

   가장 아래에는 네이버 영화 상세 정보 링크를 만들어 주세요.

   링크는 반드시 새 창에서 열려야 합니다.



### 03_datail_view

영화 상세 보기 레이아웃을 만들어 봅시다.

1. Modal

   이미지를 클릭하면, 영화에 대한 상세 정보와 추가 이미지를 보여 주도록 구성 해봅시다.

   Modal의 상단(.modal-header .modal-title)에는 영화의 한글명과 영문명을 같이 작성해 주세요.

   Modal의 헤더(.modal-header)와 내용(.modal-body) 사이에 이미지를 삽입 해주세요.

   이미지 대신 carousel로 구성 해도 됩니다.









