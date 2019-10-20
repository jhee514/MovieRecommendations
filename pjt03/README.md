# Project 03

  Project 03은 영화 추천 사이트를 제작하기 위해 HTML을 통한 웹 페이지 마크업, CSS를 통한 선택자 활용 및 속성 부여, 시맨틱 태그를 활용한 기본 레이아웃 구성, 영화 추천 사이트 메인 레이아웃 구성을 한다.



- 결과물.jpg

![결과물](./결과물.jpg)



##1. header

```html
/* header */
header {
  position: sticky;
  top: 0;
  z-index: 1000; 
}
```

  웹 사이트 헤더 부분이 항상 상단에 유지 되도록 position을 sticky 로 설정해주었다. 헤더 부분이 상단에 붙을 수 있도록 top 간격을 0으로 설정하였다. 헤더부분이 다른 부분에 가려지지 않도록 z-index 값을 1000으로 설정하여 우선순위를 높게 부여하였다.

```html
/* nav */
nav {
  float: right
}

.nav-items > li {
  display: inline-block;
  margin: 0 5px;
  list-style-type: none;
}

.nav-items > li > a {
  color: rgb(92, 92, 92);
}

.nav-items > li > a:hover {
  color:  rgb(204, 177,	85);
  text-decoration-line: none;
}
```

​	네비게이션 바는 우측에 올 수 있도록 float을  right로 설정하였다. 네비게이션 바의 리스트가 한 줄로 정렬 될 수 있도록 display를 in-line block으로 설정하였고, 리스트에 나타나는 bullet point를 제거하기 위해 list-style-type을 none으로 설정하였다. 상하 여백은 0으로, 좌우 여백은 5px로 설정하였다. 리스트 텍스트의 기본 색상은 rgb(92, 92, 92)로 설정하였고, 리스트에 마우스 오버시 색이 원하는 색으로 바뀔 수 있도록  color를 rgb(204, 177,	85)로 성정해 주었다.  리스트 밑 줄이 사라지도록 text-decoration-line은 none으로 설정하였다.



##2. title section

```html
#section-title {
  background-image: url(images/background.jpg);
  text-align: center;
  line-height: 300px;
}

.section-title-heading {
  font-size: 3rem;
  color: rgb(61,	53,	28);
}
```

  title section에 원하는 이미지가 적용될 수 있도록 background-image에 url 값을 설정해주었다. 이미지의 주소는 같은 폴더안에 위치한 images 폴더 내 backgroud.jpg로 작성하였다. 해당 텍스트가 가로선 가운데 정렬 할 수 있도록 text-align을 center로 설정하고, 세로선 가운데 정렬 할 수 있도록 line-height를 section-title 의 높이와 같은 300px로 설정하였다. 해당 텍스트의 크기는 3rem, color는 rgb(61,	53,	28)로 설정하였다.

## 3. aside

```html
aside {
  position: absolute;
  top: 0;
  bottom: 0%;
}

.aside-items {
  padding: 0;
}

.aside-items > li {
  list-style-type: none;
  color:  rgb(92, 92, 92);
}
```

  aside를 부모인 content 영역에 위치 시키기 위해 position을 absolute로 설정하여 부모 인 div#content의 position 값인 relative 값을 무시하도록 설정하였다. 상하 여백이 없도록 top, bottom을 0으로 설정하였다. 

  aside-items의 ul 태그에 자동으로 적용된 padding 값을 제거하기 위해 0으로 설정하였다. 또한 해당 리스트의 텍스트에 나오는 bullet point 제거를 위해 list-style-type을 none으로 설정, 텍스트 색깔은 rgb(92, 92, 92)로 설정하였다.



## 4. footer

```html
footer {
  /* footer는 항상 바닥에 위치하도록 position을 설정 해주세요. */
  position: fixed;
  bottom: 0;
  /* 텍스트를 가운데 정렬 해주세요. */
  text-align: center;
  /* 텍스트가 수직정렬 되도록 해주세요. (footer는 높이가 40px) */
  line-height: 40px;
  font-size: .8rem;
  background-color: rgb(204, 177,	85);
}
```

  footer의 경우 항상 바닥에 고정될 수 있도록 position을 fixed 값으로 설정 하고 bottom 여백을 0으로 하였다. 안에 위치한 텍스트가 가운데 정렬 할 수 있도록 text-align은 center, line-height는 footer와 같은 높이인 40px로 설정하였다. 텍스트 크기는 0.8rem, 배경색은  rgb(204, 177, 85)로 설정하였다.