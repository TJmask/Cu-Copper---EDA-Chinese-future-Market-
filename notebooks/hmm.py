





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-ZUjVod2EvYMDbGqRSyW0rpfgBq3i+gnR/4PfrzLsy5f20oIcRfgFQFVKgi3Ztp917bP1K/kdP5q8+nAlJ3+cFA==" rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-6548d5a1dd84bd83036c6a914b25b4ae.css" />
  
    <link crossorigin="anonymous" media="all" integrity="sha512-aX4OkLpzulpadvOncEEPpJZnQyeKNm2npzJowbL5JxptkoZXNPPy61R059xmEa3YyVF4Y4YXB6g+5o08uvdWpA==" rel="stylesheet" href="https://github.githubassets.com/assets/github-697e0e90ba73ba5a5a76f3a770410fa4.css" />
    
    
    
    


  <meta name="viewport" content="width=device-width">
  
  <title>hmmlearn/hmm.py at master · hmmlearn/hmmlearn</title>
    <meta name="description" content="Hidden Markov Models in Python, with scikit-learn like API - hmmlearn/hmmlearn">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    <meta name="twitter:image:src" content="https://avatars0.githubusercontent.com/u/7037444?s=400&amp;v=4" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary" /><meta name="twitter:title" content="hmmlearn/hmmlearn" /><meta name="twitter:description" content="Hidden Markov Models in Python, with scikit-learn like API - hmmlearn/hmmlearn" />
    <meta property="og:image" content="https://avatars0.githubusercontent.com/u/7037444?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="hmmlearn/hmmlearn" /><meta property="og:url" content="https://github.com/hmmlearn/hmmlearn" /><meta property="og:description" content="Hidden Markov Models in Python, with scikit-learn like API - hmmlearn/hmmlearn" />

  <link rel="assets" href="https://github.githubassets.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6NDg5NTE0ODEwOmQ3ZDc4NTA0M2ZhODcwZDU0MWFjOWNhYzU3ODA4ZDcxYWJjMzlmZjkxMmM5YWQ4MWVmOWE5ODY0ZDYxOWM5Njg=--efa72592cc6fac9e9fc89034b5574ba51b5acc36">
  <link rel="sudo-modal" href="/sessions/sudo_modal">

  <meta name="request-id" content="607A:5705:512D3:90A05:5E54584C" data-pjax-transient="true" /><meta name="html-safe-nonce" content="48a826697058996550a1cf80880450fe5698f881" data-pjax-transient="true" /><meta name="visitor-payload" content="eyJyZWZlcnJlciI6bnVsbCwicmVxdWVzdF9pZCI6IjYwN0E6NTcwNTo1MTJEMzo5MEEwNTo1RTU0NTg0QyIsInZpc2l0b3JfaWQiOiI1MTYxMzc1MDM4NTUwNzUwNDIxIiwicmVnaW9uX2VkZ2UiOiJpYWQiLCJyZWdpb25fcmVuZGVyIjoiaWFkIn0=" data-pjax-transient="true" /><meta name="visitor-hmac" content="4d08ca4a25b963dc210bcd1e6399bf5eab92996ab28bf82863585e3055db096b" data-pjax-transient="true" />



  <meta name="github-keyboard-shortcuts" content="repository,source-code" data-pjax-transient="true" />

  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

      <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
    <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-ga_id" content="" class="js-octo-ga-id" /><meta name="octolytics-actor-id" content="58004482" /><meta name="octolytics-actor-login" content="TJmask" /><meta name="octolytics-actor-hash" content="ceecf0465c06fdb3cd4b0e2624677fcb0ce88615856f3cbe5d2b710ada9a0373" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-2">

  <meta class="js-ga-set" name="userId" content="d6a5feea7aae25764b8d07830ba441bb">

<meta class="js-ga-set" name="dimension1" content="Logged In">



  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="TJmask">

      <meta name="expected-hostname" content="github.com">

      <meta name="js-proxy-site-detection-payload" content="YzQ1MjdmYjE3NDk3ZjIxNjI0NDBjYmMzNzllNzZlMzIxNjc1MzQ3NzcxZWY1ZmRiNzc0MzBlYjc1YTI1ZDc1ZXx7InJlbW90ZV9hZGRyZXNzIjoiMTI5LjY0LjAuMzYiLCJyZXF1ZXN0X2lkIjoiNjA3QTo1NzA1OjUxMkQzOjkwQTA1OjVFNTQ1ODRDIiwidGltZXN0YW1wIjoxNTgyNTg1OTQzLCJob3N0IjoiZ2l0aHViLmNvbSJ9">

    <meta name="enabled-features" content="MARKETPLACE_FEATURED_BLOG_POSTS,MARKETPLACE_INVOICED_BILLING,MARKETPLACE_SOCIAL_PROOF_CUSTOMERS,MARKETPLACE_TRENDING_SOCIAL_PROOF,MARKETPLACE_RECOMMENDATIONS,MARKETPLACE_PENDING_INSTALLATIONS,RELATED_ISSUES,GHE_CLOUD_TRIAL">

  <meta http-equiv="x-pjax-version" content="8310d593c1cc38b86be83242de7e6f3f">
  

      <link href="https://github.com/hmmlearn/hmmlearn/commits/master.atom" rel="alternate" title="Recent Commits to hmmlearn:master" type="application/atom+xml">

  <meta name="go-import" content="github.com/hmmlearn/hmmlearn git https://github.com/hmmlearn/hmmlearn.git">

  <meta name="octolytics-dimension-user_id" content="7037444" /><meta name="octolytics-dimension-user_login" content="hmmlearn" /><meta name="octolytics-dimension-repository_id" content="18031064" /><meta name="octolytics-dimension-repository_nwo" content="hmmlearn/hmmlearn" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="18031064" /><meta name="octolytics-dimension-repository_network_root_nwo" content="hmmlearn/hmmlearn" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


    <link rel="canonical" href="https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://github.githubassets.com/favicon.ico">

<meta name="theme-color" content="#1e2327">


  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production page-responsive page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="p-3 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <span class="Progress progress-pjax-loader position-fixed width-full js-pjax-loader-bar">
      <span class="progress-pjax-loader-bar top-0 left-0" style="width: 0%;"></span>
    </span>

    
    



          <header class="Header js-details-container Details flex-wrap flex-lg-nowrap p-responsive" role="banner">

    <div class="Header-item d-none d-lg-flex">
      <a class="Header-link" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg class="octicon octicon-mark-github v-align-middle" height="32" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
</a>

    </div>

    <div class="Header-item d-lg-none">
      <button class="Header-link btn-link js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
        <svg height="24" class="octicon octicon-three-bars" viewBox="0 0 12 16" version="1.1" width="18" aria-hidden="true"><path fill-rule="evenodd" d="M11.41 9H.59C0 9 0 8.59 0 8c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zm0-4H.59C0 5 0 4.59 0 4c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM.59 11H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1H.59C0 13 0 12.59 0 12c0-.59 0-1 .59-1z"/></svg>
      </button>
    </div>

    <div class="Header-item Header-item--full flex-column flex-lg-row width-full flex-order-2 flex-lg-order-none mr-0 mr-lg-3 mt-3 mt-lg-0 Details-content--hidden">
        <div class="header-search flex-self-stretch flex-lg-self-auto mr-0 mr-lg-3 mb-3 mb-lg-0 scoped-search site-scoped-search js-site-search position-relative js-jump-to"
  role="combobox"
  aria-owns="jump-to-results"
  aria-label="Search or jump to"
  aria-haspopup="listbox"
  aria-expanded="false"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" role="search" aria-label="Site" data-scope-type="Repository" data-scope-id="18031064" data-scoped-search-url="/hmmlearn/hmmlearn/search" data-unscoped-search-url="/search" action="/hmmlearn/hmmlearn/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
        <input type="text"
          class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search or jump to…"
          data-unscoped-placeholder="Search or jump to…"
          data-scoped-placeholder="Search or jump to…"
          autocapitalize="off"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          aria-label="Search or jump to…"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations"
          spellcheck="false"
          autocomplete="off"
          >
          <input type="hidden" value="vV+LEqWTyIkEr/9mSyFcrgSRgcCdyzb0jjJD2EuF0bqfIosiO2EJrQtUlPNZpmiQlca5OZeKGJokKk+ll/C5XQ==" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf" />
          <input type="hidden" class="js-site-search-type-field" name="type" >
            <img src="https://github.githubassets.com/images/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0013 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 000-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="text-gray">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0013 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 000-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0013 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 000-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


    <li class="d-flex flex-justify-center flex-items-center p-0 f5 js-jump-to-suggestion">
      <img src="https://github.githubassets.com/images/spinners/octocat-spinner-128.gif" alt="Octocat Spinner Icon" class="m-2" width="28">
    </li>
</ul>

            </div>
      </label>
</form>  </div>
</div>


      <nav class="d-flex flex-column flex-lg-row flex-self-stretch flex-lg-self-auto" aria-label="Global">
    <a class="Header-link d-block d-lg-none py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15" data-ga-click="Header, click, Nav menu - item:dashboard:user" aria-label="Dashboard" href="/dashboard">
      Dashboard
</a>

  <a class="js-selected-navigation-item Header-link  mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15" data-hotkey="g p" data-ga-click="Header, click, Nav menu - item:pulls context:user" aria-label="Pull requests you created" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls" href="/pulls">
    Pull requests
</a>
  <a class="js-selected-navigation-item Header-link  mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15" data-hotkey="g i" data-ga-click="Header, click, Nav menu - item:issues context:user" aria-label="Issues you created" data-selected-links="/issues /issues/assigned /issues/mentioned /issues" href="/issues">
    Issues
</a>
    <div class="mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15">
      <a class="js-selected-navigation-item Header-link" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-octo-click="marketplace_click" data-octo-dimensions="location:nav_bar" data-selected-links=" /marketplace" href="/marketplace">
        Marketplace
</a>      

    </div>

  <a class="js-selected-navigation-item Header-link  mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore" href="/explore">
    Explore
</a>


    <a class="Header-link d-block d-lg-none mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15" href="https://github.com/TJmask">
      <img class="avatar" height="20" width="20" alt="@TJmask" src="https://avatars0.githubusercontent.com/u/58004482?s=60&amp;v=4" />
      TJmask
</a>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="d4Xa2GZ+dzfSsu/UDqcTDgH/vWYw1Zyc9YOfszb1PTUo+skxFGFdSTjQnZOZUf+CqHyF2Tk3I0xeb19GugHjzw==" />
      <button type="submit" class="Header-link mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15 d-lg-none btn-link d-block width-full text-left" data-ga-click="Header, sign out, icon:logout" style="padding-left: 2px;">
        <svg class="octicon octicon-sign-out v-align-middle" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 9V7H8V5h4V3l4 3-4 3zm-2 3H6V3L2 1h8v3h1V1c0-.55-.45-1-1-1H1C.45 0 0 .45 0 1v11.38c0 .39.22.73.55.91L6 16.01V13h4c.55 0 1-.45 1-1V8h-1v4z"/></svg>
        Sign out
      </button>
</form></nav>

    </div>

    <div class="Header-item Header-item--full flex-justify-center d-lg-none position-relative">
      <div class="css-truncate css-truncate-target width-fit position-absolute left-0 right-0 text-center">
              <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
    <a class="Header-link" href="/hmmlearn">hmmlearn</a>
    /
    <a class="Header-link" href="/hmmlearn/hmmlearn">hmmlearn</a>

</div>
    </div>

    <div class="Header-item mr-0 mr-lg-3 flex-order-1 flex-lg-order-none">
      

    <a aria-label="You have no unread notifications" class="Header-link notification-indicator position-relative tooltipped tooltipped-sw js-socket-channel js-notification-indicator" data-hotkey="g n" data-ga-click="Header, go to notifications, icon:read" data-channel="notification-changed:58004482" href="/notifications/beta">
        <span class="js-indicator-modifier mail-status "></span>
        <svg class="octicon octicon-bell" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 12v1H0v-1l.73-.58c.77-.77.81-2.55 1.19-4.42C2.69 3.23 6 2 6 2c0-.55.45-1 1-1s1 .45 1 1c0 0 3.39 1.23 4.16 5 .38 1.88.42 3.66 1.19 4.42l.66.58H14zm-7 4c1.11 0 2-.89 2-2H5c0 1.11.89 2 2 2z"/></svg>
</a>
    </div>


    <div class="Header-item position-relative d-none d-lg-flex">
      <details class="details-overlay details-reset">
  <summary class="Header-link"
      aria-label="Create new…"
      data-ga-click="Header, create new, icon:add">
    <svg class="octicon octicon-plus" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5v2z"/></svg> <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw">
    
<a role="menuitem" class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a role="menuitem" class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a role="menuitem" class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a role="menuitem" class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>


  <div role="none" class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="hmmlearn/hmmlearn">This repository</span>
  </div>
    <a role="menuitem" class="dropdown-item" href="/hmmlearn/hmmlearn/issues/new" data-ga-click="Header, create new issue" data-skip-pjax>
      New issue
    </a>


  </details-menu>
</details>

    </div>

    <div class="Header-item position-relative mr-0 d-none d-lg-flex">
      
  <details class="details-overlay details-reset js-feature-preview-indicator-container" data-feature-preview-indicator-src="/users/TJmask/feature_preview/indicator_check.json">

  <summary class="Header-link"
    aria-label="View profile and more"
    data-ga-click="Header, show menu, icon:avatar">
    <img class="avatar " alt="@TJmask" width="20" height="20" src="https://avatars0.githubusercontent.com/u/58004482?s=60&amp;v=4">


      <span class="feature-preview-indicator js-feature-preview-indicator" hidden></span>
    <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw mt-2" style="width: 180px">
    <div class="header-nav-current-user css-truncate"><a role="menuitem" class="no-underline user-profile-link px-3 pt-2 pb-2 mb-n2 mt-n1 d-block" href="/TJmask" data-ga-click="Header, go to profile, text:Signed in as">Signed in as <strong class="css-truncate-target">TJmask</strong></a></div>
    <div role="none" class="dropdown-divider"></div>

      <div class="pl-3 pr-3 f6 user-status-container js-user-status-context pb-1" data-url="/users/status?compact=1&amp;link_mentions=0&amp;truncate=1">
        
<div class="js-user-status-container
    user-status-compact rounded-1 px-2 py-1 mt-2
    border
  " data-team-hovercards-enabled>
  <details class="js-user-status-details details-reset details-overlay details-overlay-dark">
    <summary class="btn-link btn-block link-gray no-underline js-toggle-user-status-edit toggle-user-status-edit "
      role="menuitem" data-hydro-click="{&quot;event_type&quot;:&quot;user_profile.click&quot;,&quot;payload&quot;:{&quot;profile_user_id&quot;:7037444,&quot;target&quot;:&quot;EDIT_USER_STATUS&quot;,&quot;user_id&quot;:58004482,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;}}" data-hydro-click-hmac="a0089d8cd0e1e3341de92e8b42d56cdc406b32cf86caaf9f91fa85bdf734590b">
      <div class="d-flex">
        <div class="f6 lh-condensed user-status-header
          d-inline-block v-align-middle
            user-status-emoji-only-header circle
            pr-2
"
            style="max-width: 29px"
          >
          <div class="user-status-emoji-container flex-shrink-0 mr-1  lh-condensed-ultra v-align-bottom" style="margin-top: 2px;">
            <div><g-emoji class="g-emoji" alias="dart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3af.png">🎯</g-emoji></div>
          </div>
        </div>
        <div class="
          d-inline-block v-align-middle
          
          
           css-truncate css-truncate-target 
           user-status-message-wrapper f6"
           style="line-height: 20px;" >
          <div class="d-inline-block text-gray-dark v-align-text-top text-left">
                <span>Focusing</span>
          </div>
        </div>
      </div>
    </summary>
    <details-dialog class="details-dialog rounded-1 anim-fade-in fast Box Box--overlay" role="dialog" tabindex="-1">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="position-relative flex-auto js-user-status-form" action="/users/status?compact=1&amp;link_mentions=0&amp;truncate=1" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="2mGf5bahchyoDQhIAx92p+MgwTKyiBl4AsudThc/2G9jo4txwfs7GME/lrcaevs6K9NnQsIOvUplKIGXoQHPvQ==" />
        <div class="Box-header bg-gray border-bottom p-3">
          <button class="Box-btn-octicon js-toggle-user-status-edit btn-octicon float-right" type="reset" aria-label="Close dialog" data-close-dialog>
            <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
          </button>
          <h3 class="Box-title f5 text-bold text-gray-dark">Edit status</h3>
        </div>
        <input type="hidden" name="emoji" class="js-user-status-emoji-field" value=":dart:">
        <input type="hidden" name="organization_id" class="js-user-status-org-id-field" value="">
        <div class="px-3 py-2 text-gray-dark">
          <div class="js-characters-remaining-container position-relative mt-2">
            <div class="input-group d-table form-group my-0 js-user-status-form-group">
              <span class="input-group-button d-table-cell v-align-middle" style="width: 1%">
                <button type="button" aria-label="Choose an emoji" class="btn-outline btn js-toggle-user-status-emoji-picker btn-open-emoji-picker p-0">
                  <span class="js-user-status-original-emoji" hidden><div><g-emoji class="g-emoji" alias="dart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3af.png">🎯</g-emoji></div></span>
                  <span class="js-user-status-custom-emoji"><div><g-emoji class="g-emoji" alias="dart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3af.png">🎯</g-emoji></div></span>
                  <span class="js-user-status-no-emoji-icon" hidden>
                    <svg class="octicon octicon-smiley" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8s3.58 8 8 8 8-3.58 8-8-3.58-8-8-8zm4.81 12.81a6.72 6.72 0 01-2.17 1.45c-.83.36-1.72.53-2.64.53-.92 0-1.81-.17-2.64-.53-.81-.34-1.55-.83-2.17-1.45a6.773 6.773 0 01-1.45-2.17A6.59 6.59 0 011.21 8c0-.92.17-1.81.53-2.64.34-.81.83-1.55 1.45-2.17.62-.62 1.36-1.11 2.17-1.45A6.59 6.59 0 018 1.21c.92 0 1.81.17 2.64.53.81.34 1.55.83 2.17 1.45.62.62 1.11 1.36 1.45 2.17.36.83.53 1.72.53 2.64 0 .92-.17 1.81-.53 2.64-.34.81-.83 1.55-1.45 2.17zM4 6.8v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2H5.2C4.53 8 4 7.47 4 6.8zm5 0v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2h-.59C9.53 8 9 7.47 9 6.8zm4 3.2c-.72 1.88-2.91 3-5 3s-4.28-1.13-5-3c-.14-.39.23-1 .66-1h8.59c.41 0 .89.61.75 1z"/></svg>
                  </span>
                </button>
              </span>
              <text-expander keys=": @" data-mention-url="/autocomplete/user-suggestions" data-emoji-url="/autocomplete/emoji">
                <input
                  type="text"
                  autocomplete="off"
                  data-no-org-url="/autocomplete/user-suggestions"
                  data-org-url="/suggestions?mention_suggester=1"
                  data-maxlength="80"
                  class="d-table-cell width-full form-control js-user-status-message-field js-characters-remaining-field"
                  placeholder="What's happening?"
                  name="message"
                  value="Focusing"
                  aria-label="What is your current status?">
              </text-expander>
              <div class="error">Could not update your status, please try again.</div>
            </div>
            <div style="margin-left: 53px" class="my-1 text-small label-characters-remaining js-characters-remaining" data-suffix="remaining" hidden>
              80 remaining
            </div>
          </div>
          <include-fragment class="js-user-status-emoji-picker" data-url="/users/status/emoji"></include-fragment>
          <div class="overflow-auto ml-n3 mr-n3 px-3 border-bottom" style="max-height: 33vh">
            <div class="user-status-suggestions js-user-status-suggestions collapsed overflow-hidden">
              <h4 class="f6 text-normal my-3">Suggestions:</h4>
              <div class="mx-3 mt-2 clearfix">
                  <div class="float-left col-6">
                      <button type="button" value=":palm_tree:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="palm_tree" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f334.png">🌴</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          On vacation
                        </div>
                      </button>
                      <button type="button" value=":face_with_thermometer:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="face_with_thermometer" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f912.png">🤒</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Out sick
                        </div>
                      </button>
                  </div>
                  <div class="float-left col-6">
                      <button type="button" value=":house:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="house" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3e0.png">🏠</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Working from home
                        </div>
                      </button>
                      <button type="button" value=":dart:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="dart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3af.png">🎯</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Focusing
                        </div>
                      </button>
                  </div>
              </div>
            </div>
            <div class="user-status-limited-availability-container">
              <div class="form-checkbox my-0">
                <input type="checkbox" name="limited_availability" value="1" class="js-user-status-limited-availability-checkbox" data-default-message="I may be slow to respond." aria-describedby="limited-availability-help-text-truncate-true-compact-true" id="limited-availability-truncate-true-compact-true">
                <label class="d-block f5 text-gray-dark mb-1" for="limited-availability-truncate-true-compact-true">
                  Busy
                </label>
                <p class="note" id="limited-availability-help-text-truncate-true-compact-true">
                  When others mention you, assign you, or request your review,
                  GitHub will let them know that you have limited availability.
                </p>
              </div>
            </div>
          </div>
          <div class="d-inline-block f5 mr-2 pt-3 pb-2" >
  <div class="d-inline-block mr-1">
    Clear status
  </div>

  <details class="js-user-status-expire-drop-down f6 dropdown details-reset details-overlay d-inline-block mr-2">
    <summary class="f5 btn-link link-gray-dark border px-2 py-1 rounded-1" aria-haspopup="true">
      <div class="js-user-status-expiration-interval-selected d-inline-block v-align-baseline">
        Never
      </div>
      <div class="dropdown-caret"></div>
    </summary>

    <ul class="dropdown-menu dropdown-menu-se pl-0 overflow-auto" style="width: 220px; max-height: 15.5em">
      <li>
        <button type="button" class="btn-link dropdown-item js-user-status-expire-button ws-normal" title="Never">
          <span class="d-inline-block text-bold mb-1">Never</span>
          <div class="f6 lh-condensed">Keep this status until you clear your status or edit your status.</div>
        </button>
      </li>
      <li class="dropdown-divider" role="none"></li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 30 minutes" value="2020-02-24T18:42:23-05:00">
            in 30 minutes
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 1 hour" value="2020-02-24T19:12:23-05:00">
            in 1 hour
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 4 hours" value="2020-02-24T22:12:23-05:00">
            in 4 hours
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="today" value="2020-02-24T23:59:59-05:00">
            today
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="this week" value="2020-03-01T23:59:59-05:00">
            this week
          </button>
        </li>
    </ul>
  </details>
  <input class="js-user-status-expiration-date-input" type="hidden" name="expires_at" value="">
</div>

          <include-fragment class="js-user-status-org-picker" data-url="/users/status/organizations"></include-fragment>
        </div>
        <div class="d-flex flex-items-center flex-justify-between p-3 border-top">
          <button type="submit"  class="width-full btn btn-primary mr-2 js-user-status-submit">
            Set status
          </button>
          <button type="button"  class="width-full js-clear-user-status-button btn ml-2 js-user-status-exists">
            Clear status
          </button>
        </div>
</form>    </details-dialog>
  </details>
</div>

      </div>
      <div role="none" class="dropdown-divider"></div>


    <a role="menuitem" class="dropdown-item" href="/TJmask" data-ga-click="Header, go to profile, text:your profile">Your profile</a>

    <a role="menuitem" class="dropdown-item" href="/TJmask?tab=repositories" data-ga-click="Header, go to repositories, text:your repositories">Your repositories</a>

    <a role="menuitem" class="dropdown-item" href="/TJmask?tab=projects" data-ga-click="Header, go to projects, text:your projects">Your projects</a>

    <a role="menuitem" class="dropdown-item" href="/TJmask?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">Your stars</a>
      <a role="menuitem" class="dropdown-item" href="https://gist.github.com/mine" data-ga-click="Header, your gists, text:your gists">Your gists</a>





    <div role="none" class="dropdown-divider"></div>
      
<div id="feature-enrollment-toggle" class="hide-sm hide-md feature-preview-details position-relative">
  <button
    type="button"
    class="dropdown-item btn-link"
    role="menuitem"
    data-feature-preview-trigger-url="/users/TJmask/feature_previews"
    data-feature-preview-close-details="{&quot;event_type&quot;:&quot;feature_preview.clicks.close_modal&quot;,&quot;payload&quot;:{&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}"
    data-feature-preview-close-hmac="5ca5b1dc09ad51506f3ea520e29705ae549a4800a13ed7265e439d3155aa5463"
    data-hydro-click="{&quot;event_type&quot;:&quot;feature_preview.clicks.open_modal&quot;,&quot;payload&quot;:{&quot;link_location&quot;:&quot;user_dropdown&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}"
    data-hydro-click-hmac="58c22592dad8a06b0d5ef2619dd6f7a9240b19808a9e756f75cbfe705bb8b334"
  >
    Feature preview
  </button>
    <span class="feature-preview-indicator js-feature-preview-indicator" hidden></span>
</div>

    <a role="menuitem" class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
    <a role="menuitem" class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">Settings</a>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="logout-form" action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="kb20FY+0UI8zII4QgNXWBAMXFfdSyiIm2gnLaaBy0LfOwqf8/at68dlC/FcXIzqIqpQtSFsonfZx5QucLIYOTQ==" />
      
      <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout" role="menuitem">
        Sign out
      </button>
      <input type="text" name="required_field_6800" hidden="hidden" class="form-control" /><input type="hidden" name="timestamp" value="1582585943665" class="form-control" /><input type="hidden" name="timestamp_secret" value="975e8453ec4bd7081b460df1e36bd54d7c227d424e41fecb9d4f5a26a9e52c5c" class="form-control" />
</form>  </details-menu>
</details>

    </div>

  </header>

      

  </div>

  <div id="start-of-content" class="show-on-focus"></div>


    <div id="js-flash-container">

</div>


      

  <include-fragment class="js-notification-shelf-include-fragment" data-base-src="https://github.com/notifications/beta/shelf"></include-fragment>




  <div class="application-main " data-commit-hovercards-enabled>
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main  >
      

  




  









  <div class="pagehead repohead hx_repohead readability-menu bg-gray-light pb-0 pt-0 pt-lg-3">

    <div class="container-lg mb-4 p-responsive d-none d-lg-flex">

      <div class="flex-auto min-width-0 width-fit mr-3">
        <h1 class="public  d-flex flex-wrap flex-items-center break-word float-none ">
    <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author ml-1 flex-self-stretch" itemprop="author">
    <a class="url fn" rel="author" data-hovercard-type="organization" data-hovercard-url="/orgs/hmmlearn/hovercard" href="/hmmlearn">hmmlearn</a>
  </span>
  <span class="path-divider flex-self-stretch">/</span>
  <strong itemprop="name" class="mr-2 flex-self-stretch">
    <a data-pjax="#js-repo-pjax-container" href="/hmmlearn/hmmlearn">hmmlearn</a>
  </strong>
  
</h1>


      </div>

      <ul class="pagehead-actions flex-shrink-0"  >



    <li >
      
    <details class="dropdown details-reset details-overlay d-inline-block float-left"
      data-deferred-details-content-url="/hmmlearn/hmmlearn/used_by_contents"
    >
      <summary class="btn btn-sm btn-with-count" data-menu-button>
        <svg class="octicon octicon-package v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1 4.27v7.47c0 .45.3.84.75.97l6.5 1.73c.16.05.34.05.5 0l6.5-1.73c.45-.13.75-.52.75-.97V4.27c0-.45-.3-.84-.75-.97l-6.5-1.74a1.4 1.4 0 00-.5 0L1.75 3.3c-.45.13-.75.52-.75.97zm7 9.09l-6-1.59V5l6 1.61v6.75zM2 4l2.5-.67L11 5.06l-2.5.67L2 4zm13 7.77l-6 1.59V6.61l2-.55V8.5l2-.53V5.53L15 5v6.77zm-2-7.24L6.5 2.8l2-.53L15 4l-2 .53z"/></svg>
        Used by
        <div class="dropdown-caret"></div>
      </summary>
      <include-fragment accept="text/fragment+html">
        <div class="dropdown-menu dropdown-menu-s p-3 text-center" style="width:360px;">
          <img width="32" height="32" alt="Loading..." class="my-0" src="https://github.githubassets.com/images/spinners/octocat-spinner-64.gif" />
          <p class="pt-1 m-0 f5 text-gray-light">
            Loading dependents...
          </p>
        </div>
      </include-fragment>
    </details>
    <a class="social-count"
      href="/hmmlearn/hmmlearn/network/dependents?package_id=UGFja2FnZS01MjIwMDk5Mg%3D%3D"
      aria-label="482 repositories depend on this package"
    >
      482
    </a>

    </li>

  <li>
    
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form data-remote="true" class="clearfix js-social-form js-social-container" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="zWYRIo3BilChTaFi5o3J68NGhcvPaRJ8icAK8esZidWGw22tigrIPEaC1u+yv16MRd7uUdJnrylex7jnf5bUeg==" />      <input type="hidden" name="repository_id" value="18031064">

      <details class="details-reset details-overlay select-menu float-left">
        <summary class="select-menu-button float-left btn btn-sm btn-with-count" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;WATCH_BUTTON&quot;,&quot;repository_id&quot;:18031064,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="9608cd5b75494dce40de2523c08e437a89c85295d48e600aef2616532b23347b" data-ga-click="Repository, click Watch settings, action:blob#show">          <span data-menu-button>
              <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
              Watch
          </span>
</summary>        <details-menu
          class="select-menu-modal position-absolute mt-5"
          style="z-index: 99;">
          <div class="select-menu-header">
            <span class="select-menu-title">Notifications</span>
          </div>
          <div class="select-menu-list">
            <button type="submit" name="do" value="included" class="select-menu-item width-full" aria-checked="true" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Not watching</span>
                <span class="description">Be notified only when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                  Watch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="release_only" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Releases only</span>
                <span class="description">Be notified of new releases, and when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                  Unwatch releases
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="subscribed" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Watching</span>
                <span class="description">Be notified of all conversations.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                  Unwatch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="ignore" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Ignoring</span>
                <span class="description">Never be notified.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-mute v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"/></svg>
                  Stop ignoring
                </span>
              </div>
            </button>
          </div>
        </details-menu>
      </details>
        <a class="social-count js-social-count"
          href="/hmmlearn/hmmlearn/watchers"
          aria-label="109 users are watching this repository">
          109
        </a>
</form>
  </li>

  <li>
      <div class="js-toggler-container js-social-container starring-container ">
    <form class="starred js-social-form" action="/hmmlearn/hmmlearn/unstar" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="AuEHx29bKogamDz0O1yBxK3ymPpWhLqa3ZZHLzlh8y3WWSoCJH+EBhJQZN2bNKZmfqF33wpUyoPxY6e38MF8HQ==" />
      <input type="hidden" name="context" value="repository"></input>
      <button type="submit" class="btn btn-sm btn-with-count js-toggler-target" aria-label="Unstar this repository" title="Unstar hmmlearn/hmmlearn" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;UNSTAR_BUTTON&quot;,&quot;repository_id&quot;:18031064,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0592d66b3cfa369b8b062167c2dd9a75429fd5bb69571484a58af21139899341" data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">        <svg aria-label="star" height="16" class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" role="img"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>

        Unstar
</button>        <a class="social-count js-social-count" href="/hmmlearn/hmmlearn/stargazers"
           aria-label="1834 users starred this repository">
           1.8k
        </a>
</form>
    <form class="unstarred js-social-form" action="/hmmlearn/hmmlearn/star" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="LIK5BEWVdVIq/RwpNM4YB7n2EWwxwYGItOypj2VDhRtZaisuSuC4ON8tdT6KRiRKwCFZUp3SwJkfE8Q+QkyqQA==" />
      <input type="hidden" name="context" value="repository"></input>
      <button type="submit" class="btn btn-sm btn-with-count js-toggler-target" aria-label="Unstar this repository" title="Star hmmlearn/hmmlearn" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;STAR_BUTTON&quot;,&quot;repository_id&quot;:18031064,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="e0343f0be406f3d3ad61c777da8fe803726cf9d8c3b206e6ef9291a31055f936" data-ga-click="Repository, click star button, action:blob#show; text:Star">        <svg aria-label="star" height="16" class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" role="img"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>

        Star
</button>        <a class="social-count js-social-count" href="/hmmlearn/hmmlearn/stargazers"
           aria-label="1834 users starred this repository">
          1.8k
        </a>
</form>  </div>

  </li>

  <li>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="btn-with-count" action="/hmmlearn/hmmlearn/fork" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="SAaNwscUb4yJtNmNtcMZ+yLWkgYr6cSrvjAy64mRTFx+EfcNRZFeoVTPPwM/CvAhzvdC6BfQn9VRXuVzZh4VoA==" />
            <button class="btn btn-sm btn-with-count" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;FORK_BUTTON&quot;,&quot;repository_id&quot;:18031064,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="61b877f965b876da6701815739beed0072f8e07d0a547c5acb5cfcc83925ae8d" data-ga-click="Repository, show fork modal, action:blob#show; text:Fork" type="submit" title="Fork your own copy of hmmlearn/hmmlearn to your account" aria-label="Fork your own copy of hmmlearn/hmmlearn to your account">              <svg class="octicon octicon-repo-forked v-align-text-bottom" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 00-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 002 1a1.993 1.993 0 00-1 3.72V6.5l3 3v1.78A1.993 1.993 0 005 15a1.993 1.993 0 001-3.72V9.5l3-3V4.72A1.993 1.993 0 008 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
              Fork
</button></form>
    <a href="/hmmlearn/hmmlearn/network/members" class="social-count"
       aria-label="555 users forked this repository">
      555
    </a>
  </li>
</ul>

    </div>
      
<nav class="hx_reponav reponav js-repo-nav js-sidenav-container-pjax clearfix container-lg p-responsive d-none d-lg-block"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
    aria-label="Repository"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /hmmlearn/hmmlearn" href="/hmmlearn/hmmlearn">
      <div class="d-inline"><svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg></div>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" data-hotkey="g i" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /hmmlearn/hmmlearn/issues" href="/hmmlearn/hmmlearn/issues">
        <div class="d-inline"><svg class="octicon octicon-issue-opened" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 011.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg></div>
        <span itemprop="name">Issues</span>
        <span class="Counter">55</span>
        <meta itemprop="position" content="2">
</a>    </span>


  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" data-skip-pjax="true" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /hmmlearn/hmmlearn/pulls" href="/hmmlearn/hmmlearn/pulls">
      <div class="d-inline"><svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0010 15a1.993 1.993 0 001-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 00-1 3.72v6.56A1.993 1.993 0 002 15a1.993 1.993 0 001-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg></div>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">2</span>
      <meta itemprop="position" content="4">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement" class="position-relative float-left">
      <a data-hotkey="g w" data-skip-pjax="true" class="js-selected-navigation-item reponav-item" data-selected-links="repo_actions /hmmlearn/hmmlearn/actions" href="/hmmlearn/hmmlearn/actions">
        <div class="d-inline"><svg class="octicon octicon-play" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 8A7 7 0 110 8a7 7 0 0114 0zm-8.223 3.482l4.599-3.066a.5.5 0 000-.832L5.777 4.518A.5.5 0 005 4.934v6.132a.5.5 0 00.777.416z"/></svg></div>
        Actions
</a>
    </span>

    <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /hmmlearn/hmmlearn/projects" href="/hmmlearn/hmmlearn/projects">
      <div class="d-inline"><svg class="octicon octicon-project" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z"/></svg></div>
      Projects
      <span class="Counter">0</span>
</a>

    <a data-skip-pjax="true" class="js-selected-navigation-item reponav-item" data-selected-links="security alerts policy token_scanning code_scanning /hmmlearn/hmmlearn/security/advisories" href="/hmmlearn/hmmlearn/security/advisories">
      <div class="d-inline"><svg class="octicon octicon-shield" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 2l7-2 7 2v6.02C14 12.69 8.69 16 7 16c-1.69 0-7-3.31-7-7.98V2zm1 .75L7 1l6 1.75v5.268C13 12.104 8.449 15 7 15c-1.449 0-6-2.896-6-6.982V2.75zm1 .75L7 2v12c-1.207 0-5-2.482-5-5.985V3.5z"/></svg></div>
      Security
</a>
    <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse people /hmmlearn/hmmlearn/pulse" href="/hmmlearn/hmmlearn/pulse">
      <div class="d-inline"><svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg></div>
      Insights
</a>

</nav>

  <div class="reponav-wrapper reponav-small d-lg-none">
  <nav class="reponav js-reponav text-center no-wrap"
       itemscope
       itemtype="http://schema.org/BreadcrumbList">

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a class="js-selected-navigation-item selected reponav-item" itemprop="url" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /hmmlearn/hmmlearn" href="/hmmlearn/hmmlearn">
        <span itemprop="name">Code</span>
        <meta itemprop="position" content="1">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /hmmlearn/hmmlearn/issues" href="/hmmlearn/hmmlearn/issues">
          <span itemprop="name">Issues</span>
          <span class="Counter">55</span>
          <meta itemprop="position" content="2">
</a>      </span>


    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /hmmlearn/hmmlearn/pulls" href="/hmmlearn/hmmlearn/pulls">
        <span itemprop="name">Pull requests</span>
        <span class="Counter">2</span>
        <meta itemprop="position" content="4">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /hmmlearn/hmmlearn/projects" href="/hmmlearn/hmmlearn/projects">
          <span itemprop="name">Projects</span>
          <span class="Counter">0</span>
          <meta itemprop="position" content="5">
</a>      </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_actions /hmmlearn/hmmlearn/actions" href="/hmmlearn/hmmlearn/actions">
          <span itemprop="name">Actions</span>
          <meta itemprop="position" content="6">
</a>      </span>


      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="security alerts policy token_scanning code_scanning /hmmlearn/hmmlearn/security/advisories" href="/hmmlearn/hmmlearn/security/advisories">
        <span itemprop="name">Security</span>
        <meta itemprop="position" content="8">
</a>
      <a class="js-selected-navigation-item reponav-item" data-selected-links="pulse /hmmlearn/hmmlearn/pulse" href="/hmmlearn/hmmlearn/pulse">
        Pulse
</a>
      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="community /hmmlearn/hmmlearn/community" href="/hmmlearn/hmmlearn/community">
          Community
</a>      </span>

  </nav>
</div>


  </div>

  

  <include-fragment class="js-notification-shelf-include-fragment" data-base-src="https://github.com/notifications/beta/shelf"></include-fragment>


<div class="container-lg clearfix new-discussion-timeline  p-responsive">
  <div class="repository-content ">

    
    


  


    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/hmmlearn/hmmlearn/blob/0e9274cb138427919c13ef79f11a7358c4e2b4a9/lib/hmmlearn/hmm.py">Permalink</a>

    <!-- blob contrib key: blob_contributors:v21:c8214e857d78ee7e7147f7676753a472 -->
      

    <div class="d-flex flex-items-start flex-shrink-0 flex-column flex-md-row pb-3">
      <span class="d-flex flex-justify-between width-full width-md-auto">
        
<details class="details-reset details-overlay branch-select-menu " id="branch-select-menu">
  <summary class="btn btn-sm css-truncate"
           data-hotkey="w"
           title="Switch branches or tags">
    <i>Branch:</i>
    <span class="css-truncate-target" data-menu-button>master</span>
    <span class="dropdown-caret"></span>
  </summary>

  <details-menu class="SelectMenu SelectMenu--hasFilter" src="/hmmlearn/hmmlearn/refs/master/lib/hmmlearn/hmm.py?source_action=show&amp;source_controller=blob" preload>
    <div class="SelectMenu-modal">
      <include-fragment class="SelectMenu-loading" aria-label="Menu is loading">
        <svg class="octicon octicon-octoface anim-pulse" height="32" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M14.7 5.34c.13-.32.55-1.59-.13-3.31 0 0-1.05-.33-3.44 1.3-1-.28-2.07-.32-3.13-.32s-2.13.04-3.13.32c-2.39-1.64-3.44-1.3-3.44-1.3-.68 1.72-.26 2.99-.13 3.31C.49 6.21 0 7.33 0 8.69 0 13.84 3.33 15 7.98 15S16 13.84 16 8.69c0-1.36-.49-2.48-1.3-3.35zM8 14.02c-3.3 0-5.98-.15-5.98-3.35 0-.76.38-1.48 1.02-2.07 1.07-.98 2.9-.46 4.96-.46 2.07 0 3.88-.52 4.96.46.65.59 1.02 1.3 1.02 2.07 0 3.19-2.68 3.35-5.98 3.35zM5.49 9.01c-.66 0-1.2.8-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.54-1.78-1.2-1.78zm5.02 0c-.66 0-1.2.79-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.53-1.78-1.2-1.78z"/></svg>
      </include-fragment>
    </div>
  </details-menu>
</details>

        <div class="BtnGroup flex-shrink-0 d-md-none">
          <a href="/hmmlearn/hmmlearn/find/master"
                class="js-pjax-capture-input btn btn-sm BtnGroup-item"
                data-pjax
                data-hotkey="t">
            Find file
          </a>
          <clipboard-copy value="lib/hmmlearn/hmm.py" class="btn btn-sm BtnGroup-item">
            Copy path
          </clipboard-copy>
        </div>
      </span>
      <h2 id="blob-path" class="breadcrumb flex-auto min-width-0 text-normal flex-md-self-center ml-md-2 mr-md-3 my-2 my-md-0">
        <span class="js-repo-root text-bold"><span class="js-path-segment"><a data-pjax="true" href="/hmmlearn/hmmlearn"><span>hmmlearn</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/hmmlearn/hmmlearn/tree/master/lib"><span>lib</span></a></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/hmmlearn/hmmlearn/tree/master/lib/hmmlearn"><span>hmmlearn</span></a></span><span class="separator">/</span><strong class="final-path">hmm.py</strong>
          <span class="separator">/</span>
          
<details class="details-reset details-overlay select-menu d-inline">
  <summary class="btn-link link-gray select-menu-button css-truncate" data-hotkey="r" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.click_on_blob_definitions&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;click_on_blob_definitions&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="57399c8686abc8704b3247848650d27a92749b75b019521135a84c31fb313bec">
    <span data-menu-button>Jump to</span>
  </summary>
  <details-menu class="select-menu-modal position-absolute" style="z-index: 99;">
    <div class="select-menu-header">
      <span class="select-menu-title">Code definitions</span>
    </div>
    <div class="select-menu-filters">
      <div class="select-menu-text-filter">
        <input
          type="text"
          id="code-def-filter-field"
          class="form-control js-filterable-field"
          placeholder="Filter definitions"
          aria-label="Filter definitions"
          autofocus
          autocomplete="off">
      </div>
    </div>
    <div class="select-menu-list lh-default" data-filterable-for="code-def-filter-field" data-filterable-type="substring">
      
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L33">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _check_and_set_gaussian_n_features
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L41">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    GaussianHMM
  </div>
  <div class="ml-1">
    Class
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L150">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    __init__
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L173">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    covars_
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L179">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    covars_
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L185">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _check
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L195">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _get_n_fit_scalars_per_param
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L210">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _init
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L227">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _compute_log_likelihood
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L231">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _generate_sample_from_state
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L237">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _initialize_sufficient_statistics
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L247">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _accumulate_sufficient_statistics
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L265">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _do_mstep
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L318">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    MultinomialHMM
  </div>
  <div class="ml-1">
    Class
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L390">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    __init__
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L403">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _get_n_fit_scalars_per_param
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L412">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _init
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L422">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _check
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L433">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _compute_log_likelihood
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L436">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _generate_sample_from_state
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L441">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _initialize_sufficient_statistics
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L446">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _accumulate_sufficient_statistics
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L454">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _do_mstep
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L460">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _check_and_set_n_features
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L478">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    GMMHMM
  </div>
  <div class="ml-1">
    Class
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L591">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    __init__
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L614">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _get_n_fit_scalars_per_param
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L631">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _init
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L676">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _init_covar_priors
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L698">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _fix_priors_shape
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L733">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _check
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L821">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _generate_sample_from_state
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L840">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _compute_log_weighted_gaussian_densities
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L851">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _compute_log_likelihood
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L862">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _initialize_sufficient_statistics
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L872">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _accumulate_sufficient_statistics
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
<a class="select-menu-item d-flex css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}" data-hydro-click-hmac="0f55a00151d0ff7051674d6304dfa4836e195f309d9b3e164dbab3b30b39128f" href="/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py#L902">
  <div class="mx-1">
    <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
  </div>
  <div class="select-menu-item-text flex-auto css-truncate-target" data-menu-button-text>
    _do_mstep
  </div>
  <div class="ml-1">
    Function
  </div>
</a>
    </div>
  </details-menu>
</details>

      </h2>

      <div class="BtnGroup flex-shrink-0 d-none d-md-inline-block">
        <a href="/hmmlearn/hmmlearn/find/master"
              class="js-pjax-capture-input btn btn-sm BtnGroup-item"
              data-pjax
              data-hotkey="t">
          Find file
        </a>
        <clipboard-copy value="lib/hmmlearn/hmm.py" class="btn btn-sm BtnGroup-item">
          Copy path
        </clipboard-copy>
      </div>
    </div>

    



    
  <div class="Box Box--condensed d-flex flex-column flex-shrink-0">
      <div class="Box-body d-flex flex-justify-between bg-blue-light flex-column flex-md-row flex-items-start flex-md-items-center">
        <span class="pr-md-4 f6">
          <a rel="contributor" data-skip-pjax="true" data-hovercard-type="user" data-hovercard-url="/users/anntzer/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/anntzer"><img class="avatar" src="https://avatars2.githubusercontent.com/u/1322974?s=40&amp;v=4" width="20" height="20" alt="@anntzer" /></a>
          <a class="text-bold link-gray-dark lh-default v-align-middle" rel="contributor" data-hovercard-type="user" data-hovercard-url="/users/anntzer/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/anntzer">anntzer</a>
            <span class="lh-default v-align-middle">
              <a data-pjax="true" title="Followup cleanup after drop of Py2 compat." class="link-gray" href="/hmmlearn/hmmlearn/commit/902ed07e427a34f5bb32ed7349b6d24745ad7cf7">Followup cleanup after drop of Py2 compat.</a>
            </span>
        </span>
        <span class="d-inline-block flex-shrink-0 v-align-bottom f6 mt-2 mt-md-0">
          <a class="pr-2 text-mono link-gray" href="/hmmlearn/hmmlearn/commit/902ed07e427a34f5bb32ed7349b6d24745ad7cf7" data-pjax>902ed07</a>
          <relative-time datetime="2019-12-15T20:47:22Z" class="no-wrap">Dec 16, 2019</relative-time>
        </span>
      </div>

    <div class="Box-body d-flex flex-items-center flex-auto f6 border-bottom-0 flex-wrap" >
      <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark float-left mr-2" id="blob_contributors_box">
        <summary class="btn-link">
          <span><strong>1</strong> contributor</span>
        </summary>
        <details-dialog
          class="Box Box--overlay d-flex flex-column anim-fade-in fast"
          aria-label="Users who have contributed to this file"
          src="/hmmlearn/hmmlearn/contributors-list/master/lib/hmmlearn/hmm.py" preload>
          <div class="Box-header">
            <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog>
              <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
            </button>
            <h3 class="Box-title">
              Users who have contributed to this file
            </h3>
          </div>
          <include-fragment class="octocat-spinner my-3" aria-label="Loading..."></include-fragment>
        </details-dialog>
      </details>
    </div>
  </div>






    <div class="Box mt-3 position-relative">
      
<div class="Box-header py-2 d-flex flex-column flex-shrink-0 flex-md-row flex-md-items-center">
  <div class="text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1 mt-2 mt-md-0">

      1014 lines (837 sloc)
      <span class="file-info-divider"></span>
    39.2 KB
  </div>

  <div class="d-flex py-1 py-md-0 flex-auto flex-order-1 flex-md-order-2 flex-sm-grow-0 flex-justify-between">

    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/hmmlearn/hmmlearn/raw/master/lib/hmmlearn/hmm.py">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/hmmlearn/hmmlearn/blame/master/lib/hmmlearn/hmm.py">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/hmmlearn/hmmlearn/commits/master/lib/hmmlearn/hmm.py">History</a>
    </div>


    <div>
          <a class="btn-octicon tooltipped tooltipped-nw js-remove-unless-platform"
             data-platforms="windows,mac"
             href="https://desktop.github.com"
             aria-label="Open this file in GitHub Desktop"
             data-ga-click="Repository, open with desktop">
              <svg class="octicon octicon-device-desktop" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M15 2H1c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5.34c-.25.61-.86 1.39-2.34 2h8c-1.48-.61-2.09-1.39-2.34-2H15c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm0 9H1V3h14v8z"/></svg>
          </a>

          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form js-update-url-with-hash" action="/hmmlearn/hmmlearn/edit/master/lib/hmmlearn/hmm.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="Zwhti+M0yGD9QZ3tueQ6XI1FXa3R3prnctBzuCbgSkWqqosXVmKwDEj1MXfovpG2cRfNHNjLD8eU9xbU5hlXMA==" />
            <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
              aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with>
              <svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 011.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
            </button>
</form>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form" action="/hmmlearn/hmmlearn/delete/master/lib/hmmlearn/hmm.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="QEeoorNCAIorESE//YSLP3s3BDaosPebJPY/mput98t/BcUAmAuFP/5mZMVHWj1PnBfO7ntqYclTbugq9mu5kw==" />
            <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
              aria-label="Fork this project and delete the file" data-disable-with>
              <svg class="octicon octicon-trashcan" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
            </button>
</form>    </div>
  </div>
</div>



        <div class="f6 v-align-middle text-gray px-3 py-2 border-bottom bg-gray-light d-flex flex-justify-between">
            <div class="d-flex text-mono">
              <svg style="color: #28a745;" class="octicon octicon-primitive-dot mr-2" viewBox="0 0 8 16" version="1.1" width="8" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 8c0-2.2 1.8-4 4-4s4 1.8 4 4-1.8 4-4 4-4-1.8-4-4z"/></svg>
              <span>You're using code navigation to jump to definitions or references.</span>
            </div>
            <div>
              <a href="https://help.github.com/en/articles/navigating-code-on-github">Learn more</a>
              or
              <a href="mailto:code-nav@github.com">give us feedback</a>
            </div>
        </div>

      

  <div itemprop="text" class="Box-body p-0 blob-wrapper data type-python ">
      
<table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class=pl-c># Hidden Markov Models</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#</span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class=pl-c># Author: Ron Weiss &lt;ronweiss@gmail.com&gt;</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#         Shiqiao Du &lt;lucidfrontier.45@gmail.com&gt;</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class=pl-c># API changes: Jaques Grobler &lt;jaquesgrobler@gmail.com&gt;</span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class=pl-c># Modifications to create of the HMMLearn module: Gael Varoquaux</span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class=pl-c># More API changes: Sergei Lebedev &lt;superbobry@gmail.com&gt;</span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class=pl-s>The :mod:`hmmlearn.hmm` module implements hidden Markov models.</span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class=pl-k>import</span> <span class=pl-s1>logging</span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line"><span class=pl-k>import</span> <span class=pl-s1>numpy</span> <span class=pl-k>as</span> <span class=pl-s1>np</span></td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class=pl-k>from</span> <span class=pl-s1>scipy</span>.<span class=pl-s1>special</span> <span class=pl-k>import</span> <span class=pl-s1>logsumexp</span></td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line"><span class=pl-k>from</span> <span class=pl-s1>sklearn</span> <span class=pl-k>import</span> <span class=pl-s1>cluster</span></td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line"><span class=pl-k>from</span> <span class=pl-s1>sklearn</span>.<span class=pl-s1>utils</span> <span class=pl-k>import</span> <span class=pl-s1>check_random_state</span></td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line"><span class=pl-k>from</span> . <span class=pl-k>import</span> <span class=pl-s1>_utils</span></td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line"><span class=pl-k>from</span> .<span class=pl-s1>stats</span> <span class=pl-k>import</span> <span class=pl-s1>log_multivariate_normal_density</span></td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line"><span class=pl-k>from</span> .<span class=pl-s1>base</span> <span class=pl-k>import</span> <span class=pl-s1>_BaseHMM</span></td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line"><span class=pl-k>from</span> .<span class=pl-s1>utils</span> <span class=pl-k>import</span> (</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">    <span class=pl-s1>fill_covars</span>, <span class=pl-s1>iter_from_X_lengths</span>, <span class=pl-s1>log_mask_zero</span>, <span class=pl-s1>log_normalize</span>, <span class=pl-s1>normalize</span>)</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>__all__</span> <span class=pl-c1>=</span> [<span class=pl-s>&quot;GMMHMM&quot;</span>, <span class=pl-s>&quot;GaussianHMM&quot;</span>, <span class=pl-s>&quot;MultinomialHMM&quot;</span>]</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line"><span class=pl-s1>_log</span> <span class=pl-c1>=</span> <span class=pl-s1>logging</span>.<span class=pl-en>getLogger</span>(<span class=pl-s1>__name__</span>)</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line"><span class=pl-v>COVARIANCE_TYPES</span> <span class=pl-c1>=</span> <span class=pl-en>frozenset</span>((<span class=pl-s>&quot;spherical&quot;</span>, <span class=pl-s>&quot;diag&quot;</span>, <span class=pl-s>&quot;full&quot;</span>, <span class=pl-s>&quot;tied&quot;</span>))</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line"><span class=pl-k>def</span> <span class=pl-en>_check_and_set_gaussian_n_features</span>(<span class=pl-s1>model</span>, <span class=pl-v>X</span>):</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">    <span class=pl-s1>_</span>, <span class=pl-s1>n_features</span> <span class=pl-c1>=</span> <span class=pl-v>X</span>.<span class=pl-s1>shape</span></td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>if</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>model</span>, <span class=pl-s>&quot;n_features&quot;</span>) <span class=pl-c1>and</span> <span class=pl-s1>model</span>.<span class=pl-s1>n_features</span> <span class=pl-c1>!=</span> <span class=pl-s1>n_features</span>:</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>raise</span> <span class=pl-v>ValueError</span>(<span class=pl-s>&quot;Unexpected number of dimensions, got {} but &quot;</span></td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">                         <span class=pl-s>&quot;expected {}&quot;</span>.<span class=pl-en>format</span>(<span class=pl-s1>n_features</span>, <span class=pl-s1>model</span>.<span class=pl-s1>n_features</span>))</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">    <span class=pl-s1>model</span>.<span class=pl-s1>n_features</span> <span class=pl-c1>=</span> <span class=pl-s1>n_features</span></td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line"><span class=pl-k>class</span> <span class=pl-v>GaussianHMM</span>(<span class=pl-s1>_BaseHMM</span>):</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">    <span class=pl-s>r&quot;&quot;&quot;Hidden Markov Model with Gaussian emissions.</span></td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    Parameters</span></td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    ----------</span></td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    n_components : int</span></td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Number of states.</span></td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    covariance_type : string, optional</span></td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        String describing the type of covariance parameters to</span></td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        use.  Must be one of</span></td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        * &quot;spherical&quot; --- each state uses a single variance value that</span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line"><span class=pl-s>          applies to all features.</span></td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        * &quot;diag&quot; --- each state uses a diagonal covariance matrix.</span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        * &quot;full&quot; --- each state uses a full (i.e. unrestricted)</span></td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line"><span class=pl-s>          covariance matrix.</span></td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        * &quot;tied&quot; --- all states use **the same** full covariance matrix.</span></td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Defaults to &quot;diag&quot;.</span></td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    min_covar : float, optional</span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Floor on the diagonal of the covariance matrix to prevent</span></td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        overfitting. Defaults to 1e-3.</span></td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    startprob_prior : array, shape (n_components, ), optional</span></td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Parameters of the Dirichlet prior distribution for</span></td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        :attr:`startprob_`.</span></td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    transmat_prior : array, shape (n_components, n_components), optional</span></td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Parameters of the Dirichlet prior distribution for each row</span></td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        of the transition probabilities :attr:`transmat_`.</span></td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    means_prior, means_weight : array, shape (n_components, ), optional</span></td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Mean and precision of the Normal prior distribtion for</span></td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        :attr:`means_`.</span></td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    covars_prior, covars_weight : array, shape (n_components, ), optional</span></td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Parameters of the prior distribution for the covariance matrix</span></td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        :attr:`covars_`.</span></td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        If :attr:`covariance_type` is &quot;spherical&quot; or &quot;diag&quot; the prior is</span></td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        the inverse gamma distribution, otherwise --- the inverse Wishart</span></td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        distribution.</span></td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    algorithm : string, optional</span></td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Decoder algorithm. Must be one of &quot;viterbi&quot; or`&quot;map&quot;.</span></td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Defaults to &quot;viterbi&quot;.</span></td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    random_state: RandomState or an int seed, optional</span></td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        A random number generator instance.</span></td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    n_iter : int, optional</span></td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Maximum number of iterations to perform.</span></td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    tol : float, optional</span></td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Convergence threshold. EM will stop if the gain in log-likelihood</span></td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        is below this value.</span></td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    verbose : bool, optional</span></td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        When ``True`` per-iteration convergence reports are printed</span></td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        to :data:`sys.stderr`. You can diagnose convergence via the</span></td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        :attr:`monitor_` attribute.</span></td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    params : string, optional</span></td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Controls which parameters are updated in the training</span></td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        process.  Can contain any combination of &#39;s&#39; for startprob,</span></td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &#39;t&#39; for transmat, &#39;m&#39; for means and &#39;c&#39; for covars. Defaults</span></td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        to all parameters.</span></td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    init_params : string, optional</span></td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Controls which parameters are initialized prior to</span></td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        training.  Can contain any combination of &#39;s&#39; for</span></td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        startprob, &#39;t&#39; for transmat, &#39;m&#39; for means and &#39;c&#39; for covars.</span></td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Defaults to all parameters.</span></td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    Attributes</span></td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    ----------</span></td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    n_features : int</span></td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Dimensionality of the Gaussian emissions.</span></td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    monitor\_ : ConvergenceMonitor</span></td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Monitor object used to check the convergence of EM.</span></td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    startprob\_ : array, shape (n_components, )</span></td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Initial state occupation distribution.</span></td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    transmat\_ : array, shape (n_components, n_components)</span></td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Matrix of transition probabilities between states.</span></td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    means\_ : array, shape (n_components, n_features)</span></td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Mean parameters for each state.</span></td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    covars\_ : array</span></td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Covariance parameters for each state.</span></td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        The shape depends on :attr:`covariance_type`::</span></td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line"><span class=pl-s>            (n_components, )                        if &quot;spherical&quot;,</span></td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line"><span class=pl-s>            (n_components, n_features)              if &quot;diag&quot;,</span></td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line"><span class=pl-s>            (n_components, n_features, n_features)  if &quot;full&quot;</span></td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line"><span class=pl-s>            (n_features, n_features)                if &quot;tied&quot;,</span></td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    Examples</span></td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    --------</span></td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    &gt;&gt;&gt; from hmmlearn.hmm import GaussianHMM</span></td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    &gt;&gt;&gt; GaussianHMM(n_components=2)  #doctest: +ELLIPSIS</span></td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    GaussianHMM(algorithm=&#39;viterbi&#39;,...</span></td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>__init__</span>(<span class=pl-s1>self</span>, <span class=pl-s1>n_components</span><span class=pl-c1>=</span><span class=pl-c1>1</span>, <span class=pl-s1>covariance_type</span><span class=pl-c1>=</span><span class=pl-s>&#39;diag&#39;</span>,</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">                 <span class=pl-s1>min_covar</span><span class=pl-c1>=</span><span class=pl-c1>1e-3</span>,</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">                 <span class=pl-s1>startprob_prior</span><span class=pl-c1>=</span><span class=pl-c1>1.0</span>, <span class=pl-s1>transmat_prior</span><span class=pl-c1>=</span><span class=pl-c1>1.0</span>,</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">                 <span class=pl-s1>means_prior</span><span class=pl-c1>=</span><span class=pl-c1>0</span>, <span class=pl-s1>means_weight</span><span class=pl-c1>=</span><span class=pl-c1>0</span>,</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">                 <span class=pl-s1>covars_prior</span><span class=pl-c1>=</span><span class=pl-c1>1e-2</span>, <span class=pl-s1>covars_weight</span><span class=pl-c1>=</span><span class=pl-c1>1</span>,</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">                 <span class=pl-s1>algorithm</span><span class=pl-c1>=</span><span class=pl-s>&quot;viterbi&quot;</span>, <span class=pl-s1>random_state</span><span class=pl-c1>=</span><span class=pl-c1>None</span>,</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">                 <span class=pl-s1>n_iter</span><span class=pl-c1>=</span><span class=pl-c1>10</span>, <span class=pl-s1>tol</span><span class=pl-c1>=</span><span class=pl-c1>1e-2</span>, <span class=pl-s1>verbose</span><span class=pl-c1>=</span><span class=pl-c1>False</span>,</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">                 <span class=pl-s1>params</span><span class=pl-c1>=</span><span class=pl-s>&quot;stmc&quot;</span>, <span class=pl-s1>init_params</span><span class=pl-c1>=</span><span class=pl-s>&quot;stmc&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>_BaseHMM</span>.<span class=pl-en>__init__</span>(<span class=pl-s1>self</span>, <span class=pl-s1>n_components</span>,</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">                          <span class=pl-s1>startprob_prior</span><span class=pl-c1>=</span><span class=pl-s1>startprob_prior</span>,</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">                          <span class=pl-s1>transmat_prior</span><span class=pl-c1>=</span><span class=pl-s1>transmat_prior</span>, <span class=pl-s1>algorithm</span><span class=pl-c1>=</span><span class=pl-s1>algorithm</span>,</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">                          <span class=pl-s1>random_state</span><span class=pl-c1>=</span><span class=pl-s1>random_state</span>, <span class=pl-s1>n_iter</span><span class=pl-c1>=</span><span class=pl-s1>n_iter</span>,</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">                          <span class=pl-s1>tol</span><span class=pl-c1>=</span><span class=pl-s1>tol</span>, <span class=pl-s1>params</span><span class=pl-c1>=</span><span class=pl-s1>params</span>, <span class=pl-s1>verbose</span><span class=pl-c1>=</span><span class=pl-s1>verbose</span>,</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">                          <span class=pl-s1>init_params</span><span class=pl-c1>=</span><span class=pl-s1>init_params</span>)</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>=</span> <span class=pl-s1>covariance_type</span></td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>min_covar</span> <span class=pl-c1>=</span> <span class=pl-s1>min_covar</span></td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>means_prior</span> <span class=pl-c1>=</span> <span class=pl-s1>means_prior</span></td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>means_weight</span> <span class=pl-c1>=</span> <span class=pl-s1>means_weight</span></td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span> <span class=pl-c1>=</span> <span class=pl-s1>covars_prior</span></td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span> <span class=pl-c1>=</span> <span class=pl-s1>covars_weight</span></td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">    <span class=pl-en>@<span class=pl-s1>property</span></span></td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>covars_</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;Return covars as a full matrix.&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-en>fill_covars</span>(<span class=pl-s1>self</span>.<span class=pl-s1>_covars_</span>, <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span>,</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">                           <span class=pl-s1>self</span>.<span class=pl-s1>n_components</span>, <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span>)</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">    <span class=pl-en>@<span class=pl-s1>covars_</span>.<span class=pl-s1>setter</span></span></td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>covars_</span>(<span class=pl-s1>self</span>, <span class=pl-s1>covars</span>):</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>covars</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>array</span>(<span class=pl-s1>covars</span>, <span class=pl-s1>copy</span><span class=pl-c1>=</span><span class=pl-c1>True</span>)</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>_utils</span>.<span class=pl-en>_validate_covars</span>(<span class=pl-s1>covars</span>, <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span>,</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">                                <span class=pl-s1>self</span>.<span class=pl-s1>n_components</span>)</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>_covars_</span> <span class=pl-c1>=</span> <span class=pl-s1>covars</span></td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_check</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">        <span class=pl-en>super</span>().<span class=pl-en>_check</span>()</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>means_</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>asarray</span>(<span class=pl-s1>self</span>.<span class=pl-s1>means_</span>)</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>means_</span>.<span class=pl-s1>shape</span>[<span class=pl-c1>1</span>]</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>not</span> <span class=pl-c1>in</span> <span class=pl-v>COVARIANCE_TYPES</span>:</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>raise</span> <span class=pl-v>ValueError</span>(<span class=pl-s>&#39;covariance_type must be one of {}&#39;</span></td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">                             .<span class=pl-en>format</span>(<span class=pl-v>COVARIANCE_TYPES</span>))</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_get_n_fit_scalars_per_param</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>nc</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_components</span></td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>nf</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span></td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> {</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&quot;s&quot;</span>: <span class=pl-s1>nc</span> <span class=pl-c1>-</span> <span class=pl-c1>1</span>,</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&quot;t&quot;</span>: <span class=pl-s1>nc</span> <span class=pl-c1>*</span> (<span class=pl-s1>nc</span> <span class=pl-c1>-</span> <span class=pl-c1>1</span>),</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&quot;m&quot;</span>: <span class=pl-s1>nc</span> <span class=pl-c1>*</span> <span class=pl-s1>nf</span>,</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&quot;c&quot;</span>: {</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">                <span class=pl-s>&quot;spherical&quot;</span>: <span class=pl-s1>nc</span>,</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">                <span class=pl-s>&quot;diag&quot;</span>: <span class=pl-s1>nc</span> <span class=pl-c1>*</span> <span class=pl-s1>nf</span>,</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">                <span class=pl-s>&quot;full&quot;</span>: <span class=pl-s1>nc</span> <span class=pl-c1>*</span> <span class=pl-s1>nf</span> <span class=pl-c1>*</span> (<span class=pl-s1>nf</span> <span class=pl-c1>+</span> <span class=pl-c1>1</span>) <span class=pl-c1>//</span> <span class=pl-c1>2</span>,</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">                <span class=pl-s>&quot;tied&quot;</span>: <span class=pl-s1>nf</span> <span class=pl-c1>*</span> (<span class=pl-s1>nf</span> <span class=pl-c1>+</span> <span class=pl-c1>1</span>) <span class=pl-c1>//</span> <span class=pl-c1>2</span>,</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">            }[<span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span>],</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">        }</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_init</span>(<span class=pl-s1>self</span>, <span class=pl-v>X</span>, <span class=pl-s1>lengths</span><span class=pl-c1>=</span><span class=pl-c1>None</span>):</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">        <span class=pl-en>_check_and_set_gaussian_n_features</span>(<span class=pl-s1>self</span>, <span class=pl-v>X</span>)</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">        <span class=pl-en>super</span>().<span class=pl-en>_init</span>(<span class=pl-v>X</span>, <span class=pl-s1>lengths</span><span class=pl-c1>=</span><span class=pl-s1>lengths</span>)</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s>&#39;m&#39;</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>init_params</span> <span class=pl-c1>or</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&quot;means_&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>kmeans</span> <span class=pl-c1>=</span> <span class=pl-s1>cluster</span>.<span class=pl-v>KMeans</span>(<span class=pl-s1>n_clusters</span><span class=pl-c1>=</span><span class=pl-s1>self</span>.<span class=pl-s1>n_components</span>,</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">                                    <span class=pl-s1>random_state</span><span class=pl-c1>=</span><span class=pl-s1>self</span>.<span class=pl-s1>random_state</span>)</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>kmeans</span>.<span class=pl-en>fit</span>(<span class=pl-v>X</span>)</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>means_</span> <span class=pl-c1>=</span> <span class=pl-s1>kmeans</span>.<span class=pl-s1>cluster_centers_</span></td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s>&#39;c&#39;</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>init_params</span> <span class=pl-c1>or</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&quot;covars_&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>cv</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>cov</span>(<span class=pl-v>X</span>.<span class=pl-v>T</span>) <span class=pl-c1>+</span> <span class=pl-s1>self</span>.<span class=pl-s1>min_covar</span> <span class=pl-c1>*</span> <span class=pl-s1>np</span>.<span class=pl-en>eye</span>(<span class=pl-v>X</span>.<span class=pl-s1>shape</span>[<span class=pl-c1>1</span>])</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-s1>cv</span>.<span class=pl-s1>shape</span>:</td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>cv</span>.<span class=pl-s1>shape</span> <span class=pl-c1>=</span> (<span class=pl-c1>1</span>, <span class=pl-c1>1</span>)</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>covars_</span> <span class=pl-c1>=</span> \</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>_utils</span>.<span class=pl-en>distribute_covar_matrix_to_match_covariance_type</span>(</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>cv</span>, <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span>, <span class=pl-s1>self</span>.<span class=pl-s1>n_components</span>).<span class=pl-en>copy</span>()</td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_compute_log_likelihood</span>(<span class=pl-s1>self</span>, <span class=pl-v>X</span>):</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-en>log_multivariate_normal_density</span>(</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">            <span class=pl-v>X</span>, <span class=pl-s1>self</span>.<span class=pl-s1>means_</span>, <span class=pl-s1>self</span>.<span class=pl-s1>_covars_</span>, <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span>)</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_generate_sample_from_state</span>(<span class=pl-s1>self</span>, <span class=pl-s1>state</span>, <span class=pl-s1>random_state</span><span class=pl-c1>=</span><span class=pl-c1>None</span>):</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>random_state</span> <span class=pl-c1>=</span> <span class=pl-en>check_random_state</span>(<span class=pl-s1>random_state</span>)</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>random_state</span>.<span class=pl-en>multivariate_normal</span>(</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>means_</span>[<span class=pl-s1>state</span>], <span class=pl-s1>self</span>.<span class=pl-s1>covars_</span>[<span class=pl-s1>state</span>]</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_initialize_sufficient_statistics</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>stats</span> <span class=pl-c1>=</span> <span class=pl-en>super</span>().<span class=pl-en>_initialize_sufficient_statistics</span>()</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post&#39;</span>] <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>zeros</span>(<span class=pl-s1>self</span>.<span class=pl-s1>n_components</span>)</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>stats</span>[<span class=pl-s>&#39;obs&#39;</span>] <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>zeros</span>((<span class=pl-s1>self</span>.<span class=pl-s1>n_components</span>, <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span>))</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>stats</span>[<span class=pl-s>&#39;obs**2&#39;</span>] <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>zeros</span>((<span class=pl-s1>self</span>.<span class=pl-s1>n_components</span>, <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span>))</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>in</span> (<span class=pl-s>&#39;tied&#39;</span>, <span class=pl-s>&#39;full&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>stats</span>[<span class=pl-s>&#39;obs*obs.T&#39;</span>] <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>zeros</span>((<span class=pl-s1>self</span>.<span class=pl-s1>n_components</span>, <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span>,</td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">                                           <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span>))</td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>stats</span></td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_accumulate_sufficient_statistics</span>(<span class=pl-s1>self</span>, <span class=pl-s1>stats</span>, <span class=pl-s1>obs</span>, <span class=pl-s1>framelogprob</span>,</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">                                          <span class=pl-s1>posteriors</span>, <span class=pl-s1>fwdlattice</span>, <span class=pl-s1>bwdlattice</span>):</td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">        <span class=pl-en>super</span>().<span class=pl-en>_accumulate_sufficient_statistics</span>(</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>stats</span>, <span class=pl-s1>obs</span>, <span class=pl-s1>framelogprob</span>, <span class=pl-s1>posteriors</span>, <span class=pl-s1>fwdlattice</span>, <span class=pl-s1>bwdlattice</span>)</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s>&#39;m&#39;</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>params</span> <span class=pl-c1>or</span> <span class=pl-s>&#39;c&#39;</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>params</span>:</td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post&#39;</span>] <span class=pl-c1>+=</span> <span class=pl-s1>posteriors</span>.<span class=pl-en>sum</span>(<span class=pl-s1>axis</span><span class=pl-c1>=</span><span class=pl-c1>0</span>)</td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>stats</span>[<span class=pl-s>&#39;obs&#39;</span>] <span class=pl-c1>+=</span> <span class=pl-s1>np</span>.<span class=pl-en>dot</span>(<span class=pl-s1>posteriors</span>.<span class=pl-v>T</span>, <span class=pl-s1>obs</span>)</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s>&#39;c&#39;</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>params</span>:</td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>in</span> (<span class=pl-s>&#39;spherical&#39;</span>, <span class=pl-s>&#39;diag&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>stats</span>[<span class=pl-s>&#39;obs**2&#39;</span>] <span class=pl-c1>+=</span> <span class=pl-s1>np</span>.<span class=pl-en>dot</span>(<span class=pl-s1>posteriors</span>.<span class=pl-v>T</span>, <span class=pl-s1>obs</span> <span class=pl-c1>**</span> <span class=pl-c1>2</span>)</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>elif</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>in</span> (<span class=pl-s>&#39;tied&#39;</span>, <span class=pl-s>&#39;full&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">                <span class=pl-c># posteriors: (nt, nc); obs: (nt, nf); obs: (nt, nf)</span></td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">                <span class=pl-c># -&gt; (nc, nf, nf)</span></td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>stats</span>[<span class=pl-s>&#39;obs*obs.T&#39;</span>] <span class=pl-c1>+=</span> <span class=pl-s1>np</span>.<span class=pl-en>einsum</span>(</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s>&#39;ij,ik,il-&gt;jkl&#39;</span>, <span class=pl-s1>posteriors</span>, <span class=pl-s1>obs</span>, <span class=pl-s1>obs</span>)</td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_do_mstep</span>(<span class=pl-s1>self</span>, <span class=pl-s1>stats</span>):</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">        <span class=pl-en>super</span>().<span class=pl-en>_do_mstep</span>(<span class=pl-s1>stats</span>)</td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>means_prior</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>means_prior</span></td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>means_weight</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>means_weight</span></td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># TODO: find a proper reference for estimates for different</span></td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">        <span class=pl-c>#       covariance models.</span></td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Based on Huang, Acero, Hon, &quot;Spoken Language Processing&quot;,</span></td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># p. 443 - 445</span></td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>denom</span> <span class=pl-c1>=</span> <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post&#39;</span>][:, <span class=pl-s1>np</span>.<span class=pl-s1>newaxis</span>]</td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s>&#39;m&#39;</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>params</span>:</td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>means_</span> <span class=pl-c1>=</span> ((<span class=pl-s1>means_weight</span> <span class=pl-c1>*</span> <span class=pl-s1>means_prior</span> <span class=pl-c1>+</span> <span class=pl-s1>stats</span>[<span class=pl-s>&#39;obs&#39;</span>])</td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line">                           <span class=pl-c1>/</span> (<span class=pl-s1>means_weight</span> <span class=pl-c1>+</span> <span class=pl-s1>denom</span>))</td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s>&#39;c&#39;</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>params</span>:</td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>covars_prior</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span></td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>covars_weight</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span></td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>meandiff</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>means_</span> <span class=pl-c1>-</span> <span class=pl-s1>means_prior</span></td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>in</span> (<span class=pl-s>&#39;spherical&#39;</span>, <span class=pl-s>&#39;diag&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>cv_num</span> <span class=pl-c1>=</span> (<span class=pl-s1>means_weight</span> <span class=pl-c1>*</span> <span class=pl-s1>meandiff</span><span class=pl-c1>**</span><span class=pl-c1>2</span></td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line">                          <span class=pl-c1>+</span> <span class=pl-s1>stats</span>[<span class=pl-s>&#39;obs**2&#39;</span>]</td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">                          <span class=pl-c1>-</span> <span class=pl-c1>2</span> <span class=pl-c1>*</span> <span class=pl-s1>self</span>.<span class=pl-s1>means_</span> <span class=pl-c1>*</span> <span class=pl-s1>stats</span>[<span class=pl-s>&#39;obs&#39;</span>]</td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">                          <span class=pl-c1>+</span> <span class=pl-s1>self</span>.<span class=pl-s1>means_</span><span class=pl-c1>**</span><span class=pl-c1>2</span> <span class=pl-c1>*</span> <span class=pl-s1>denom</span>)</td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>cv_den</span> <span class=pl-c1>=</span> <span class=pl-en>max</span>(<span class=pl-s1>covars_weight</span> <span class=pl-c1>-</span> <span class=pl-c1>1</span>, <span class=pl-c1>0</span>) <span class=pl-c1>+</span> <span class=pl-s1>denom</span></td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>_covars_</span> <span class=pl-c1>=</span> \</td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line">                    (<span class=pl-s1>covars_prior</span> <span class=pl-c1>+</span> <span class=pl-s1>cv_num</span>) <span class=pl-c1>/</span> <span class=pl-s1>np</span>.<span class=pl-en>maximum</span>(<span class=pl-s1>cv_den</span>, <span class=pl-c1>1e-5</span>)</td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;spherical&#39;</span>:</td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>self</span>.<span class=pl-s1>_covars_</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>tile</span>(</td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">                        <span class=pl-s1>self</span>.<span class=pl-s1>_covars_</span>.<span class=pl-en>mean</span>(<span class=pl-c1>1</span>)[:, <span class=pl-s1>np</span>.<span class=pl-s1>newaxis</span>],</td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line">                        (<span class=pl-c1>1</span>, <span class=pl-s1>self</span>.<span class=pl-s1>_covars_</span>.<span class=pl-s1>shape</span>[<span class=pl-c1>1</span>]))</td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>elif</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>in</span> (<span class=pl-s>&#39;tied&#39;</span>, <span class=pl-s>&#39;full&#39;</span>):</td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>cv_num</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>empty</span>((<span class=pl-s1>self</span>.<span class=pl-s1>n_components</span>, <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span>,</td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line">                                  <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span>))</td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>for</span> <span class=pl-s1>c</span> <span class=pl-c1>in</span> <span class=pl-en>range</span>(<span class=pl-s1>self</span>.<span class=pl-s1>n_components</span>):</td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>obsmean</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>outer</span>(<span class=pl-s1>stats</span>[<span class=pl-s>&#39;obs&#39;</span>][<span class=pl-s1>c</span>], <span class=pl-s1>self</span>.<span class=pl-s1>means_</span>[<span class=pl-s1>c</span>])</td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>cv_num</span>[<span class=pl-s1>c</span>] <span class=pl-c1>=</span> (<span class=pl-s1>means_weight</span> <span class=pl-c1>*</span> <span class=pl-s1>np</span>.<span class=pl-en>outer</span>(<span class=pl-s1>meandiff</span>[<span class=pl-s1>c</span>],</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line">                                                         <span class=pl-s1>meandiff</span>[<span class=pl-s1>c</span>])</td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line">                                 <span class=pl-c1>+</span> <span class=pl-s1>stats</span>[<span class=pl-s>&#39;obs*obs.T&#39;</span>][<span class=pl-s1>c</span>]</td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line">                                 <span class=pl-c1>-</span> <span class=pl-s1>obsmean</span> <span class=pl-c1>-</span> <span class=pl-s1>obsmean</span>.<span class=pl-v>T</span></td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line">                                 <span class=pl-c1>+</span> <span class=pl-s1>np</span>.<span class=pl-en>outer</span>(<span class=pl-s1>self</span>.<span class=pl-s1>means_</span>[<span class=pl-s1>c</span>], <span class=pl-s1>self</span>.<span class=pl-s1>means_</span>[<span class=pl-s1>c</span>])</td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line">                                 <span class=pl-c1>*</span> <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post&#39;</span>][<span class=pl-s1>c</span>])</td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>cvweight</span> <span class=pl-c1>=</span> <span class=pl-en>max</span>(<span class=pl-s1>covars_weight</span> <span class=pl-c1>-</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span>, <span class=pl-c1>0</span>)</td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;tied&#39;</span>:</td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>self</span>.<span class=pl-s1>_covars_</span> <span class=pl-c1>=</span> ((<span class=pl-s1>covars_prior</span> <span class=pl-c1>+</span> <span class=pl-s1>cv_num</span>.<span class=pl-en>sum</span>(<span class=pl-s1>axis</span><span class=pl-c1>=</span><span class=pl-c1>0</span>)) <span class=pl-c1>/</span></td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line">                                     (<span class=pl-s1>cvweight</span> <span class=pl-c1>+</span> <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post&#39;</span>].<span class=pl-en>sum</span>()))</td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>elif</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;full&#39;</span>:</td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>self</span>.<span class=pl-s1>_covars_</span> <span class=pl-c1>=</span> ((<span class=pl-s1>covars_prior</span> <span class=pl-c1>+</span> <span class=pl-s1>cv_num</span>) <span class=pl-c1>/</span></td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line">                                     (<span class=pl-s1>cvweight</span> <span class=pl-c1>+</span> <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post&#39;</span>][:, <span class=pl-c1>None</span>, <span class=pl-c1>None</span>]))</td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line"><span class=pl-k>class</span> <span class=pl-v>MultinomialHMM</span>(<span class=pl-s1>_BaseHMM</span>):</td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line">    <span class=pl-s>r&quot;&quot;&quot;Hidden Markov Model with multinomial (discrete) emissions</span></td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    Parameters</span></td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    ----------</span></td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    n_components : int</span></td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Number of states.</span></td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    startprob_prior : array, shape (n_components, ), optional</span></td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Parameters of the Dirichlet prior distribution for</span></td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        :attr:`startprob_`.</span></td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    transmat_prior : array, shape (n_components, n_components), optional</span></td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Parameters of the Dirichlet prior distribution for each row</span></td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        of the transition probabilities :attr:`transmat_`.</span></td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    algorithm : string, optional</span></td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Decoder algorithm. Must be one of &quot;viterbi&quot; or &quot;map&quot;.</span></td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Defaults to &quot;viterbi&quot;.</span></td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    random_state: RandomState or an int seed, optional</span></td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        A random number generator instance.</span></td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    n_iter : int, optional</span></td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Maximum number of iterations to perform.</span></td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    tol : float, optional</span></td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Convergence threshold. EM will stop if the gain in log-likelihood</span></td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        is below this value.</span></td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    verbose : bool, optional</span></td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        When ``True`` per-iteration convergence reports are printed</span></td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        to :data:`sys.stderr`. You can diagnose convergence via the</span></td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        :attr:`monitor_` attribute.</span></td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    params : string, optional</span></td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Controls which parameters are updated in the training</span></td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        process.  Can contain any combination of &#39;s&#39; for startprob,</span></td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &#39;t&#39; for transmat, &#39;e&#39; for emissionprob.</span></td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Defaults to all parameters.</span></td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    init_params : string, optional</span></td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Controls which parameters are initialized prior to</span></td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        training.  Can contain any combination of &#39;s&#39; for</span></td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        startprob, &#39;t&#39; for transmat, &#39;e&#39; for emissionprob.</span></td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Defaults to all parameters.</span></td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    Attributes</span></td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    ----------</span></td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    n_features : int</span></td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Number of possible symbols emitted by the model (in the samples).</span></td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    monitor\_ : ConvergenceMonitor</span></td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Monitor object used to check the convergence of EM.</span></td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    startprob\_ : array, shape (n_components, )</span></td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Initial state occupation distribution.</span></td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    transmat\_ : array, shape (n_components, n_components)</span></td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Matrix of transition probabilities between states.</span></td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    emissionprob\_ : array, shape (n_components, n_features)</span></td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Probability of emitting a given symbol when in each state.</span></td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    Examples</span></td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    --------</span></td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    &gt;&gt;&gt; from hmmlearn.hmm import MultinomialHMM</span></td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    &gt;&gt;&gt; MultinomialHMM(n_components=2)  #doctest: +ELLIPSIS</span></td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    MultinomialHMM(algorithm=&#39;viterbi&#39;,...</span></td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code blob-code-inner js-file-line">    <span class=pl-c># TODO: accept the prior on emissionprob_ for consistency.</span></td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>__init__</span>(<span class=pl-s1>self</span>, <span class=pl-s1>n_components</span><span class=pl-c1>=</span><span class=pl-c1>1</span>,</td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code blob-code-inner js-file-line">                 <span class=pl-s1>startprob_prior</span><span class=pl-c1>=</span><span class=pl-c1>1.0</span>, <span class=pl-s1>transmat_prior</span><span class=pl-c1>=</span><span class=pl-c1>1.0</span>,</td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code blob-code-inner js-file-line">                 <span class=pl-s1>algorithm</span><span class=pl-c1>=</span><span class=pl-s>&quot;viterbi&quot;</span>, <span class=pl-s1>random_state</span><span class=pl-c1>=</span><span class=pl-c1>None</span>,</td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code blob-code-inner js-file-line">                 <span class=pl-s1>n_iter</span><span class=pl-c1>=</span><span class=pl-c1>10</span>, <span class=pl-s1>tol</span><span class=pl-c1>=</span><span class=pl-c1>1e-2</span>, <span class=pl-s1>verbose</span><span class=pl-c1>=</span><span class=pl-c1>False</span>,</td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code blob-code-inner js-file-line">                 <span class=pl-s1>params</span><span class=pl-c1>=</span><span class=pl-s>&quot;ste&quot;</span>, <span class=pl-s1>init_params</span><span class=pl-c1>=</span><span class=pl-s>&quot;ste&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>_BaseHMM</span>.<span class=pl-en>__init__</span>(<span class=pl-s1>self</span>, <span class=pl-s1>n_components</span>,</td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code blob-code-inner js-file-line">                          <span class=pl-s1>startprob_prior</span><span class=pl-c1>=</span><span class=pl-s1>startprob_prior</span>,</td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code blob-code-inner js-file-line">                          <span class=pl-s1>transmat_prior</span><span class=pl-c1>=</span><span class=pl-s1>transmat_prior</span>,</td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code blob-code-inner js-file-line">                          <span class=pl-s1>algorithm</span><span class=pl-c1>=</span><span class=pl-s1>algorithm</span>,</td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code blob-code-inner js-file-line">                          <span class=pl-s1>random_state</span><span class=pl-c1>=</span><span class=pl-s1>random_state</span>,</td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code blob-code-inner js-file-line">                          <span class=pl-s1>n_iter</span><span class=pl-c1>=</span><span class=pl-s1>n_iter</span>, <span class=pl-s1>tol</span><span class=pl-c1>=</span><span class=pl-s1>tol</span>, <span class=pl-s1>verbose</span><span class=pl-c1>=</span><span class=pl-s1>verbose</span>,</td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code blob-code-inner js-file-line">                          <span class=pl-s1>params</span><span class=pl-c1>=</span><span class=pl-s1>params</span>, <span class=pl-s1>init_params</span><span class=pl-c1>=</span><span class=pl-s1>init_params</span>)</td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_get_n_fit_scalars_per_param</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>nc</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_components</span></td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>nf</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span></td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> {</td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&quot;s&quot;</span>: <span class=pl-s1>nc</span> <span class=pl-c1>-</span> <span class=pl-c1>1</span>,</td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&quot;t&quot;</span>: <span class=pl-s1>nc</span> <span class=pl-c1>*</span> (<span class=pl-s1>nc</span> <span class=pl-c1>-</span> <span class=pl-c1>1</span>),</td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&quot;e&quot;</span>: <span class=pl-s1>nc</span> <span class=pl-c1>*</span> (<span class=pl-s1>nf</span> <span class=pl-c1>-</span> <span class=pl-c1>1</span>),</td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code blob-code-inner js-file-line">        }</td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_init</span>(<span class=pl-s1>self</span>, <span class=pl-v>X</span>, <span class=pl-s1>lengths</span><span class=pl-c1>=</span><span class=pl-c1>None</span>):</td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-en>_check_and_set_n_features</span>(<span class=pl-v>X</span>)</td>
      </tr>
      <tr>
        <td id="L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="LC414" class="blob-code blob-code-inner js-file-line">        <span class=pl-en>super</span>().<span class=pl-en>_init</span>(<span class=pl-v>X</span>, <span class=pl-s1>lengths</span><span class=pl-c1>=</span><span class=pl-s1>lengths</span>)</td>
      </tr>
      <tr>
        <td id="L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="LC415" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>random_state</span> <span class=pl-c1>=</span> <span class=pl-en>check_random_state</span>(<span class=pl-s1>self</span>.<span class=pl-s1>random_state</span>)</td>
      </tr>
      <tr>
        <td id="L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="LC416" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="LC417" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s>&#39;e&#39;</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>init_params</span>:</td>
      </tr>
      <tr>
        <td id="L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="LC418" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>emissionprob_</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>random_state</span> \</td>
      </tr>
      <tr>
        <td id="L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="LC419" class="blob-code blob-code-inner js-file-line">                .<span class=pl-en>rand</span>(<span class=pl-s1>self</span>.<span class=pl-s1>n_components</span>, <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span>)</td>
      </tr>
      <tr>
        <td id="L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="LC420" class="blob-code blob-code-inner js-file-line">            <span class=pl-en>normalize</span>(<span class=pl-s1>self</span>.<span class=pl-s1>emissionprob_</span>, <span class=pl-s1>axis</span><span class=pl-c1>=</span><span class=pl-c1>1</span>)</td>
      </tr>
      <tr>
        <td id="L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="LC421" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="LC422" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_check</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="LC423" class="blob-code blob-code-inner js-file-line">        <span class=pl-en>super</span>().<span class=pl-en>_check</span>()</td>
      </tr>
      <tr>
        <td id="L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="LC424" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="LC425" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>emissionprob_</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>atleast_2d</span>(<span class=pl-s1>self</span>.<span class=pl-s1>emissionprob_</span>)</td>
      </tr>
      <tr>
        <td id="L426" class="blob-num js-line-number" data-line-number="426"></td>
        <td id="LC426" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>n_features</span> <span class=pl-c1>=</span> <span class=pl-en>getattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&quot;n_features&quot;</span>, <span class=pl-s1>self</span>.<span class=pl-s1>emissionprob_</span>.<span class=pl-s1>shape</span>[<span class=pl-c1>1</span>])</td>
      </tr>
      <tr>
        <td id="L427" class="blob-num js-line-number" data-line-number="427"></td>
        <td id="LC427" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>emissionprob_</span>.<span class=pl-s1>shape</span> <span class=pl-c1>!=</span> (<span class=pl-s1>self</span>.<span class=pl-s1>n_components</span>, <span class=pl-s1>n_features</span>):</td>
      </tr>
      <tr>
        <td id="L428" class="blob-num js-line-number" data-line-number="428"></td>
        <td id="LC428" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>raise</span> <span class=pl-v>ValueError</span>(</td>
      </tr>
      <tr>
        <td id="L429" class="blob-num js-line-number" data-line-number="429"></td>
        <td id="LC429" class="blob-code blob-code-inner js-file-line">                <span class=pl-s>&quot;emissionprob_ must have shape (n_components, n_features)&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L430" class="blob-num js-line-number" data-line-number="430"></td>
        <td id="LC430" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>else</span>:</td>
      </tr>
      <tr>
        <td id="L431" class="blob-num js-line-number" data-line-number="431"></td>
        <td id="LC431" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span> <span class=pl-c1>=</span> <span class=pl-s1>n_features</span></td>
      </tr>
      <tr>
        <td id="L432" class="blob-num js-line-number" data-line-number="432"></td>
        <td id="LC432" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L433" class="blob-num js-line-number" data-line-number="433"></td>
        <td id="LC433" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_compute_log_likelihood</span>(<span class=pl-s1>self</span>, <span class=pl-v>X</span>):</td>
      </tr>
      <tr>
        <td id="L434" class="blob-num js-line-number" data-line-number="434"></td>
        <td id="LC434" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-en>log_mask_zero</span>(<span class=pl-s1>self</span>.<span class=pl-s1>emissionprob_</span>)[:, <span class=pl-s1>np</span>.<span class=pl-en>concatenate</span>(<span class=pl-v>X</span>)].<span class=pl-v>T</span></td>
      </tr>
      <tr>
        <td id="L435" class="blob-num js-line-number" data-line-number="435"></td>
        <td id="LC435" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L436" class="blob-num js-line-number" data-line-number="436"></td>
        <td id="LC436" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_generate_sample_from_state</span>(<span class=pl-s1>self</span>, <span class=pl-s1>state</span>, <span class=pl-s1>random_state</span><span class=pl-c1>=</span><span class=pl-c1>None</span>):</td>
      </tr>
      <tr>
        <td id="L437" class="blob-num js-line-number" data-line-number="437"></td>
        <td id="LC437" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>cdf</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>cumsum</span>(<span class=pl-s1>self</span>.<span class=pl-s1>emissionprob_</span>[<span class=pl-s1>state</span>, :])</td>
      </tr>
      <tr>
        <td id="L438" class="blob-num js-line-number" data-line-number="438"></td>
        <td id="LC438" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>random_state</span> <span class=pl-c1>=</span> <span class=pl-en>check_random_state</span>(<span class=pl-s1>random_state</span>)</td>
      </tr>
      <tr>
        <td id="L439" class="blob-num js-line-number" data-line-number="439"></td>
        <td id="LC439" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> [(<span class=pl-s1>cdf</span> <span class=pl-c1>&gt;</span> <span class=pl-s1>random_state</span>.<span class=pl-en>rand</span>()).<span class=pl-en>argmax</span>()]</td>
      </tr>
      <tr>
        <td id="L440" class="blob-num js-line-number" data-line-number="440"></td>
        <td id="LC440" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L441" class="blob-num js-line-number" data-line-number="441"></td>
        <td id="LC441" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_initialize_sufficient_statistics</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L442" class="blob-num js-line-number" data-line-number="442"></td>
        <td id="LC442" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>stats</span> <span class=pl-c1>=</span> <span class=pl-en>super</span>().<span class=pl-en>_initialize_sufficient_statistics</span>()</td>
      </tr>
      <tr>
        <td id="L443" class="blob-num js-line-number" data-line-number="443"></td>
        <td id="LC443" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>stats</span>[<span class=pl-s>&#39;obs&#39;</span>] <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>zeros</span>((<span class=pl-s1>self</span>.<span class=pl-s1>n_components</span>, <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span>))</td>
      </tr>
      <tr>
        <td id="L444" class="blob-num js-line-number" data-line-number="444"></td>
        <td id="LC444" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>stats</span></td>
      </tr>
      <tr>
        <td id="L445" class="blob-num js-line-number" data-line-number="445"></td>
        <td id="LC445" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L446" class="blob-num js-line-number" data-line-number="446"></td>
        <td id="LC446" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_accumulate_sufficient_statistics</span>(<span class=pl-s1>self</span>, <span class=pl-s1>stats</span>, <span class=pl-v>X</span>, <span class=pl-s1>framelogprob</span>,</td>
      </tr>
      <tr>
        <td id="L447" class="blob-num js-line-number" data-line-number="447"></td>
        <td id="LC447" class="blob-code blob-code-inner js-file-line">                                          <span class=pl-s1>posteriors</span>, <span class=pl-s1>fwdlattice</span>, <span class=pl-s1>bwdlattice</span>):</td>
      </tr>
      <tr>
        <td id="L448" class="blob-num js-line-number" data-line-number="448"></td>
        <td id="LC448" class="blob-code blob-code-inner js-file-line">        <span class=pl-en>super</span>().<span class=pl-en>_accumulate_sufficient_statistics</span>(</td>
      </tr>
      <tr>
        <td id="L449" class="blob-num js-line-number" data-line-number="449"></td>
        <td id="LC449" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>stats</span>, <span class=pl-v>X</span>, <span class=pl-s1>framelogprob</span>, <span class=pl-s1>posteriors</span>, <span class=pl-s1>fwdlattice</span>, <span class=pl-s1>bwdlattice</span>)</td>
      </tr>
      <tr>
        <td id="L450" class="blob-num js-line-number" data-line-number="450"></td>
        <td id="LC450" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s>&#39;e&#39;</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>params</span>:</td>
      </tr>
      <tr>
        <td id="L451" class="blob-num js-line-number" data-line-number="451"></td>
        <td id="LC451" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>t</span>, <span class=pl-s1>symbol</span> <span class=pl-c1>in</span> <span class=pl-en>enumerate</span>(<span class=pl-s1>np</span>.<span class=pl-en>concatenate</span>(<span class=pl-v>X</span>)):</td>
      </tr>
      <tr>
        <td id="L452" class="blob-num js-line-number" data-line-number="452"></td>
        <td id="LC452" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>stats</span>[<span class=pl-s>&#39;obs&#39;</span>][:, <span class=pl-s1>symbol</span>] <span class=pl-c1>+=</span> <span class=pl-s1>posteriors</span>[<span class=pl-s1>t</span>]</td>
      </tr>
      <tr>
        <td id="L453" class="blob-num js-line-number" data-line-number="453"></td>
        <td id="LC453" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L454" class="blob-num js-line-number" data-line-number="454"></td>
        <td id="LC454" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_do_mstep</span>(<span class=pl-s1>self</span>, <span class=pl-s1>stats</span>):</td>
      </tr>
      <tr>
        <td id="L455" class="blob-num js-line-number" data-line-number="455"></td>
        <td id="LC455" class="blob-code blob-code-inner js-file-line">        <span class=pl-en>super</span>().<span class=pl-en>_do_mstep</span>(<span class=pl-s1>stats</span>)</td>
      </tr>
      <tr>
        <td id="L456" class="blob-num js-line-number" data-line-number="456"></td>
        <td id="LC456" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s>&#39;e&#39;</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>params</span>:</td>
      </tr>
      <tr>
        <td id="L457" class="blob-num js-line-number" data-line-number="457"></td>
        <td id="LC457" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>emissionprob_</span> <span class=pl-c1>=</span> (<span class=pl-s1>stats</span>[<span class=pl-s>&#39;obs&#39;</span>]</td>
      </tr>
      <tr>
        <td id="L458" class="blob-num js-line-number" data-line-number="458"></td>
        <td id="LC458" class="blob-code blob-code-inner js-file-line">                                  <span class=pl-c1>/</span> <span class=pl-s1>stats</span>[<span class=pl-s>&#39;obs&#39;</span>].<span class=pl-en>sum</span>(<span class=pl-s1>axis</span><span class=pl-c1>=</span><span class=pl-c1>1</span>)[:, <span class=pl-s1>np</span>.<span class=pl-s1>newaxis</span>])</td>
      </tr>
      <tr>
        <td id="L459" class="blob-num js-line-number" data-line-number="459"></td>
        <td id="LC459" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L460" class="blob-num js-line-number" data-line-number="460"></td>
        <td id="LC460" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_check_and_set_n_features</span>(<span class=pl-s1>self</span>, <span class=pl-v>X</span>):</td>
      </tr>
      <tr>
        <td id="L461" class="blob-num js-line-number" data-line-number="461"></td>
        <td id="LC461" class="blob-code blob-code-inner js-file-line">        <span class=pl-s>&quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L462" class="blob-num js-line-number" data-line-number="462"></td>
        <td id="LC462" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Check if ``X`` is a sample from a Multinomial distribution, i.e. an</span></td>
      </tr>
      <tr>
        <td id="L463" class="blob-num js-line-number" data-line-number="463"></td>
        <td id="LC463" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        array of non-negative integers.</span></td>
      </tr>
      <tr>
        <td id="L464" class="blob-num js-line-number" data-line-number="464"></td>
        <td id="LC464" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L465" class="blob-num js-line-number" data-line-number="465"></td>
        <td id="LC465" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-s1>np</span>.<span class=pl-en>issubdtype</span>(<span class=pl-v>X</span>.<span class=pl-s1>dtype</span>, <span class=pl-s1>np</span>.<span class=pl-s1>integer</span>):</td>
      </tr>
      <tr>
        <td id="L466" class="blob-num js-line-number" data-line-number="466"></td>
        <td id="LC466" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>raise</span> <span class=pl-v>ValueError</span>(<span class=pl-s>&quot;Symbols should be integers&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L467" class="blob-num js-line-number" data-line-number="467"></td>
        <td id="LC467" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-v>X</span>.<span class=pl-en>min</span>() <span class=pl-c1>&lt;</span> <span class=pl-c1>0</span>:</td>
      </tr>
      <tr>
        <td id="L468" class="blob-num js-line-number" data-line-number="468"></td>
        <td id="LC468" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>raise</span> <span class=pl-v>ValueError</span>(<span class=pl-s>&quot;Symbols should be nonnegative&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L469" class="blob-num js-line-number" data-line-number="469"></td>
        <td id="LC469" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&quot;n_features&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L470" class="blob-num js-line-number" data-line-number="470"></td>
        <td id="LC470" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span> <span class=pl-c1>-</span> <span class=pl-c1>1</span> <span class=pl-c1>&lt;</span> <span class=pl-v>X</span>.<span class=pl-en>max</span>():</td>
      </tr>
      <tr>
        <td id="L471" class="blob-num js-line-number" data-line-number="471"></td>
        <td id="LC471" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>raise</span> <span class=pl-v>ValueError</span>(</td>
      </tr>
      <tr>
        <td id="L472" class="blob-num js-line-number" data-line-number="472"></td>
        <td id="LC472" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s>&quot;Largest symbol is {} but the model only emits &quot;</span></td>
      </tr>
      <tr>
        <td id="L473" class="blob-num js-line-number" data-line-number="473"></td>
        <td id="LC473" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s>&quot;symbols up to {}&quot;</span></td>
      </tr>
      <tr>
        <td id="L474" class="blob-num js-line-number" data-line-number="474"></td>
        <td id="LC474" class="blob-code blob-code-inner js-file-line">                    .<span class=pl-en>format</span>(<span class=pl-v>X</span>.<span class=pl-en>max</span>(), <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span> <span class=pl-c1>-</span> <span class=pl-c1>1</span>))</td>
      </tr>
      <tr>
        <td id="L475" class="blob-num js-line-number" data-line-number="475"></td>
        <td id="LC475" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span> <span class=pl-c1>=</span> <span class=pl-v>X</span>.<span class=pl-en>max</span>() <span class=pl-c1>+</span> <span class=pl-c1>1</span></td>
      </tr>
      <tr>
        <td id="L476" class="blob-num js-line-number" data-line-number="476"></td>
        <td id="LC476" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L477" class="blob-num js-line-number" data-line-number="477"></td>
        <td id="LC477" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L478" class="blob-num js-line-number" data-line-number="478"></td>
        <td id="LC478" class="blob-code blob-code-inner js-file-line"><span class=pl-k>class</span> <span class=pl-v>GMMHMM</span>(<span class=pl-s1>_BaseHMM</span>):</td>
      </tr>
      <tr>
        <td id="L479" class="blob-num js-line-number" data-line-number="479"></td>
        <td id="LC479" class="blob-code blob-code-inner js-file-line">    <span class=pl-s>r&quot;&quot;&quot;Hidden Markov Model with Gaussian mixture emissions.</span></td>
      </tr>
      <tr>
        <td id="L480" class="blob-num js-line-number" data-line-number="480"></td>
        <td id="LC480" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L481" class="blob-num js-line-number" data-line-number="481"></td>
        <td id="LC481" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    Parameters</span></td>
      </tr>
      <tr>
        <td id="L482" class="blob-num js-line-number" data-line-number="482"></td>
        <td id="LC482" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    ----------</span></td>
      </tr>
      <tr>
        <td id="L483" class="blob-num js-line-number" data-line-number="483"></td>
        <td id="LC483" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    n_components : int</span></td>
      </tr>
      <tr>
        <td id="L484" class="blob-num js-line-number" data-line-number="484"></td>
        <td id="LC484" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Number of states in the model.</span></td>
      </tr>
      <tr>
        <td id="L485" class="blob-num js-line-number" data-line-number="485"></td>
        <td id="LC485" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L486" class="blob-num js-line-number" data-line-number="486"></td>
        <td id="LC486" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    n_mix : int</span></td>
      </tr>
      <tr>
        <td id="L487" class="blob-num js-line-number" data-line-number="487"></td>
        <td id="LC487" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Number of states in the GMM.</span></td>
      </tr>
      <tr>
        <td id="L488" class="blob-num js-line-number" data-line-number="488"></td>
        <td id="LC488" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L489" class="blob-num js-line-number" data-line-number="489"></td>
        <td id="LC489" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    covariance_type : string, optional</span></td>
      </tr>
      <tr>
        <td id="L490" class="blob-num js-line-number" data-line-number="490"></td>
        <td id="LC490" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        String describing the type of covariance parameters to</span></td>
      </tr>
      <tr>
        <td id="L491" class="blob-num js-line-number" data-line-number="491"></td>
        <td id="LC491" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        use.  Must be one of</span></td>
      </tr>
      <tr>
        <td id="L492" class="blob-num js-line-number" data-line-number="492"></td>
        <td id="LC492" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L493" class="blob-num js-line-number" data-line-number="493"></td>
        <td id="LC493" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        * &quot;spherical&quot; --- each state uses a single variance value that</span></td>
      </tr>
      <tr>
        <td id="L494" class="blob-num js-line-number" data-line-number="494"></td>
        <td id="LC494" class="blob-code blob-code-inner js-file-line"><span class=pl-s>          applies to all features.</span></td>
      </tr>
      <tr>
        <td id="L495" class="blob-num js-line-number" data-line-number="495"></td>
        <td id="LC495" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        * &quot;diag&quot; --- each state uses a diagonal covariance matrix.</span></td>
      </tr>
      <tr>
        <td id="L496" class="blob-num js-line-number" data-line-number="496"></td>
        <td id="LC496" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        * &quot;full&quot; --- each state uses a full (i.e. unrestricted)</span></td>
      </tr>
      <tr>
        <td id="L497" class="blob-num js-line-number" data-line-number="497"></td>
        <td id="LC497" class="blob-code blob-code-inner js-file-line"><span class=pl-s>          covariance matrix.</span></td>
      </tr>
      <tr>
        <td id="L498" class="blob-num js-line-number" data-line-number="498"></td>
        <td id="LC498" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        * &quot;tied&quot; --- all mixture components of each state use **the same** full</span></td>
      </tr>
      <tr>
        <td id="L499" class="blob-num js-line-number" data-line-number="499"></td>
        <td id="LC499" class="blob-code blob-code-inner js-file-line"><span class=pl-s>          covariance matrix (note that this is not the same as for</span></td>
      </tr>
      <tr>
        <td id="L500" class="blob-num js-line-number" data-line-number="500"></td>
        <td id="LC500" class="blob-code blob-code-inner js-file-line"><span class=pl-s>          `GaussianHMM`).</span></td>
      </tr>
      <tr>
        <td id="L501" class="blob-num js-line-number" data-line-number="501"></td>
        <td id="LC501" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L502" class="blob-num js-line-number" data-line-number="502"></td>
        <td id="LC502" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Defaults to &quot;diag&quot;.</span></td>
      </tr>
      <tr>
        <td id="L503" class="blob-num js-line-number" data-line-number="503"></td>
        <td id="LC503" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L504" class="blob-num js-line-number" data-line-number="504"></td>
        <td id="LC504" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    min_covar : float, optional</span></td>
      </tr>
      <tr>
        <td id="L505" class="blob-num js-line-number" data-line-number="505"></td>
        <td id="LC505" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Floor on the diagonal of the covariance matrix to prevent</span></td>
      </tr>
      <tr>
        <td id="L506" class="blob-num js-line-number" data-line-number="506"></td>
        <td id="LC506" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        overfitting. Defaults to 1e-3.</span></td>
      </tr>
      <tr>
        <td id="L507" class="blob-num js-line-number" data-line-number="507"></td>
        <td id="LC507" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L508" class="blob-num js-line-number" data-line-number="508"></td>
        <td id="LC508" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    startprob_prior : array, shape (n_components, ), optional</span></td>
      </tr>
      <tr>
        <td id="L509" class="blob-num js-line-number" data-line-number="509"></td>
        <td id="LC509" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Parameters of the Dirichlet prior distribution for</span></td>
      </tr>
      <tr>
        <td id="L510" class="blob-num js-line-number" data-line-number="510"></td>
        <td id="LC510" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        :attr:`startprob_`.</span></td>
      </tr>
      <tr>
        <td id="L511" class="blob-num js-line-number" data-line-number="511"></td>
        <td id="LC511" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L512" class="blob-num js-line-number" data-line-number="512"></td>
        <td id="LC512" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    transmat_prior : array, shape (n_components, n_components), optional</span></td>
      </tr>
      <tr>
        <td id="L513" class="blob-num js-line-number" data-line-number="513"></td>
        <td id="LC513" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Parameters of the Dirichlet prior distribution for each row</span></td>
      </tr>
      <tr>
        <td id="L514" class="blob-num js-line-number" data-line-number="514"></td>
        <td id="LC514" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        of the transition probabilities :attr:`transmat_`.</span></td>
      </tr>
      <tr>
        <td id="L515" class="blob-num js-line-number" data-line-number="515"></td>
        <td id="LC515" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L516" class="blob-num js-line-number" data-line-number="516"></td>
        <td id="LC516" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    weights_prior : array, shape (n_mix, ), optional</span></td>
      </tr>
      <tr>
        <td id="L517" class="blob-num js-line-number" data-line-number="517"></td>
        <td id="LC517" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Parameters of the Dirichlet prior distribution for</span></td>
      </tr>
      <tr>
        <td id="L518" class="blob-num js-line-number" data-line-number="518"></td>
        <td id="LC518" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        :attr:`weights_`.</span></td>
      </tr>
      <tr>
        <td id="L519" class="blob-num js-line-number" data-line-number="519"></td>
        <td id="LC519" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L520" class="blob-num js-line-number" data-line-number="520"></td>
        <td id="LC520" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    means_prior, means_weight : array, shape (n_mix, ), optional</span></td>
      </tr>
      <tr>
        <td id="L521" class="blob-num js-line-number" data-line-number="521"></td>
        <td id="LC521" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Mean and precision of the Normal prior distribtion for</span></td>
      </tr>
      <tr>
        <td id="L522" class="blob-num js-line-number" data-line-number="522"></td>
        <td id="LC522" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        :attr:`means_`.</span></td>
      </tr>
      <tr>
        <td id="L523" class="blob-num js-line-number" data-line-number="523"></td>
        <td id="LC523" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L524" class="blob-num js-line-number" data-line-number="524"></td>
        <td id="LC524" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    covars_prior, covars_weight : array, shape (n_mix, ), optional</span></td>
      </tr>
      <tr>
        <td id="L525" class="blob-num js-line-number" data-line-number="525"></td>
        <td id="LC525" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Parameters of the prior distribution for the covariance matrix</span></td>
      </tr>
      <tr>
        <td id="L526" class="blob-num js-line-number" data-line-number="526"></td>
        <td id="LC526" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        :attr:`covars_`.</span></td>
      </tr>
      <tr>
        <td id="L527" class="blob-num js-line-number" data-line-number="527"></td>
        <td id="LC527" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L528" class="blob-num js-line-number" data-line-number="528"></td>
        <td id="LC528" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        If :attr:`covariance_type` is &quot;spherical&quot; or &quot;diag&quot; the prior is</span></td>
      </tr>
      <tr>
        <td id="L529" class="blob-num js-line-number" data-line-number="529"></td>
        <td id="LC529" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        the inverse gamma distribution, otherwise --- the inverse Wishart</span></td>
      </tr>
      <tr>
        <td id="L530" class="blob-num js-line-number" data-line-number="530"></td>
        <td id="LC530" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        distribution.</span></td>
      </tr>
      <tr>
        <td id="L531" class="blob-num js-line-number" data-line-number="531"></td>
        <td id="LC531" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L532" class="blob-num js-line-number" data-line-number="532"></td>
        <td id="LC532" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    algorithm : string, optional</span></td>
      </tr>
      <tr>
        <td id="L533" class="blob-num js-line-number" data-line-number="533"></td>
        <td id="LC533" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Decoder algorithm. Must be one of &quot;viterbi&quot; or &quot;map&quot;.</span></td>
      </tr>
      <tr>
        <td id="L534" class="blob-num js-line-number" data-line-number="534"></td>
        <td id="LC534" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Defaults to &quot;viterbi&quot;.</span></td>
      </tr>
      <tr>
        <td id="L535" class="blob-num js-line-number" data-line-number="535"></td>
        <td id="LC535" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L536" class="blob-num js-line-number" data-line-number="536"></td>
        <td id="LC536" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    random_state: RandomState or an int seed, optional</span></td>
      </tr>
      <tr>
        <td id="L537" class="blob-num js-line-number" data-line-number="537"></td>
        <td id="LC537" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        A random number generator instance.</span></td>
      </tr>
      <tr>
        <td id="L538" class="blob-num js-line-number" data-line-number="538"></td>
        <td id="LC538" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L539" class="blob-num js-line-number" data-line-number="539"></td>
        <td id="LC539" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    n_iter : int, optional</span></td>
      </tr>
      <tr>
        <td id="L540" class="blob-num js-line-number" data-line-number="540"></td>
        <td id="LC540" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Maximum number of iterations to perform.</span></td>
      </tr>
      <tr>
        <td id="L541" class="blob-num js-line-number" data-line-number="541"></td>
        <td id="LC541" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L542" class="blob-num js-line-number" data-line-number="542"></td>
        <td id="LC542" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    tol : float, optional</span></td>
      </tr>
      <tr>
        <td id="L543" class="blob-num js-line-number" data-line-number="543"></td>
        <td id="LC543" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Convergence threshold. EM will stop if the gain in log-likelihood</span></td>
      </tr>
      <tr>
        <td id="L544" class="blob-num js-line-number" data-line-number="544"></td>
        <td id="LC544" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        is below this value.</span></td>
      </tr>
      <tr>
        <td id="L545" class="blob-num js-line-number" data-line-number="545"></td>
        <td id="LC545" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L546" class="blob-num js-line-number" data-line-number="546"></td>
        <td id="LC546" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    verbose : bool, optional</span></td>
      </tr>
      <tr>
        <td id="L547" class="blob-num js-line-number" data-line-number="547"></td>
        <td id="LC547" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        When ``True`` per-iteration convergence reports are printed</span></td>
      </tr>
      <tr>
        <td id="L548" class="blob-num js-line-number" data-line-number="548"></td>
        <td id="LC548" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        to :data:`sys.stderr`. You can diagnose convergence via the</span></td>
      </tr>
      <tr>
        <td id="L549" class="blob-num js-line-number" data-line-number="549"></td>
        <td id="LC549" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        :attr:`monitor_` attribute.</span></td>
      </tr>
      <tr>
        <td id="L550" class="blob-num js-line-number" data-line-number="550"></td>
        <td id="LC550" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L551" class="blob-num js-line-number" data-line-number="551"></td>
        <td id="LC551" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    init_params : string, optional</span></td>
      </tr>
      <tr>
        <td id="L552" class="blob-num js-line-number" data-line-number="552"></td>
        <td id="LC552" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Controls which parameters are initialized prior to training. Can</span></td>
      </tr>
      <tr>
        <td id="L553" class="blob-num js-line-number" data-line-number="553"></td>
        <td id="LC553" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        contain any combination of &#39;s&#39; for startprob, &#39;t&#39; for transmat, &#39;m&#39;</span></td>
      </tr>
      <tr>
        <td id="L554" class="blob-num js-line-number" data-line-number="554"></td>
        <td id="LC554" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        for means, &#39;c&#39; for covars, and &#39;w&#39; for GMM mixing weights.</span></td>
      </tr>
      <tr>
        <td id="L555" class="blob-num js-line-number" data-line-number="555"></td>
        <td id="LC555" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Defaults to all parameters.</span></td>
      </tr>
      <tr>
        <td id="L556" class="blob-num js-line-number" data-line-number="556"></td>
        <td id="LC556" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L557" class="blob-num js-line-number" data-line-number="557"></td>
        <td id="LC557" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    params : string, optional</span></td>
      </tr>
      <tr>
        <td id="L558" class="blob-num js-line-number" data-line-number="558"></td>
        <td id="LC558" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Controls which parameters are updated in the training process.  Can</span></td>
      </tr>
      <tr>
        <td id="L559" class="blob-num js-line-number" data-line-number="559"></td>
        <td id="LC559" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        contain any combination of &#39;s&#39; for startprob, &#39;t&#39; for transmat, &#39;m&#39; for</span></td>
      </tr>
      <tr>
        <td id="L560" class="blob-num js-line-number" data-line-number="560"></td>
        <td id="LC560" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        means, and &#39;c&#39; for covars, and &#39;w&#39; for GMM mixing weights.</span></td>
      </tr>
      <tr>
        <td id="L561" class="blob-num js-line-number" data-line-number="561"></td>
        <td id="LC561" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Defaults to all parameters.</span></td>
      </tr>
      <tr>
        <td id="L562" class="blob-num js-line-number" data-line-number="562"></td>
        <td id="LC562" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L563" class="blob-num js-line-number" data-line-number="563"></td>
        <td id="LC563" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    Attributes</span></td>
      </tr>
      <tr>
        <td id="L564" class="blob-num js-line-number" data-line-number="564"></td>
        <td id="LC564" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    ----------</span></td>
      </tr>
      <tr>
        <td id="L565" class="blob-num js-line-number" data-line-number="565"></td>
        <td id="LC565" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    monitor\_ : ConvergenceMonitor</span></td>
      </tr>
      <tr>
        <td id="L566" class="blob-num js-line-number" data-line-number="566"></td>
        <td id="LC566" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Monitor object used to check the convergence of EM.</span></td>
      </tr>
      <tr>
        <td id="L567" class="blob-num js-line-number" data-line-number="567"></td>
        <td id="LC567" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L568" class="blob-num js-line-number" data-line-number="568"></td>
        <td id="LC568" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    startprob\_ : array, shape (n_components, )</span></td>
      </tr>
      <tr>
        <td id="L569" class="blob-num js-line-number" data-line-number="569"></td>
        <td id="LC569" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Initial state occupation distribution.</span></td>
      </tr>
      <tr>
        <td id="L570" class="blob-num js-line-number" data-line-number="570"></td>
        <td id="LC570" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L571" class="blob-num js-line-number" data-line-number="571"></td>
        <td id="LC571" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    transmat\_ : array, shape (n_components, n_components)</span></td>
      </tr>
      <tr>
        <td id="L572" class="blob-num js-line-number" data-line-number="572"></td>
        <td id="LC572" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Matrix of transition probabilities between states.</span></td>
      </tr>
      <tr>
        <td id="L573" class="blob-num js-line-number" data-line-number="573"></td>
        <td id="LC573" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L574" class="blob-num js-line-number" data-line-number="574"></td>
        <td id="LC574" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    weights\_ : array, shape (n_components, n_mix)</span></td>
      </tr>
      <tr>
        <td id="L575" class="blob-num js-line-number" data-line-number="575"></td>
        <td id="LC575" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Mixture weights for each state.</span></td>
      </tr>
      <tr>
        <td id="L576" class="blob-num js-line-number" data-line-number="576"></td>
        <td id="LC576" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L577" class="blob-num js-line-number" data-line-number="577"></td>
        <td id="LC577" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    means\_ : array, shape (n_components, n_mix)</span></td>
      </tr>
      <tr>
        <td id="L578" class="blob-num js-line-number" data-line-number="578"></td>
        <td id="LC578" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Mean parameters for each mixture component in each state.</span></td>
      </tr>
      <tr>
        <td id="L579" class="blob-num js-line-number" data-line-number="579"></td>
        <td id="LC579" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L580" class="blob-num js-line-number" data-line-number="580"></td>
        <td id="LC580" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    covars\_ : array</span></td>
      </tr>
      <tr>
        <td id="L581" class="blob-num js-line-number" data-line-number="581"></td>
        <td id="LC581" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        Covariance parameters for each mixture components in each state.</span></td>
      </tr>
      <tr>
        <td id="L582" class="blob-num js-line-number" data-line-number="582"></td>
        <td id="LC582" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L583" class="blob-num js-line-number" data-line-number="583"></td>
        <td id="LC583" class="blob-code blob-code-inner js-file-line"><span class=pl-s>        The shape depends on :attr:`covariance_type`::</span></td>
      </tr>
      <tr>
        <td id="L584" class="blob-num js-line-number" data-line-number="584"></td>
        <td id="LC584" class="blob-code blob-code-inner js-file-line"><span class=pl-s></span></td>
      </tr>
      <tr>
        <td id="L585" class="blob-num js-line-number" data-line-number="585"></td>
        <td id="LC585" class="blob-code blob-code-inner js-file-line"><span class=pl-s>            (n_components, n_mix)                          if &quot;spherical&quot;,</span></td>
      </tr>
      <tr>
        <td id="L586" class="blob-num js-line-number" data-line-number="586"></td>
        <td id="LC586" class="blob-code blob-code-inner js-file-line"><span class=pl-s>            (n_components, n_mix, n_features)              if &quot;diag&quot;,</span></td>
      </tr>
      <tr>
        <td id="L587" class="blob-num js-line-number" data-line-number="587"></td>
        <td id="LC587" class="blob-code blob-code-inner js-file-line"><span class=pl-s>            (n_components, n_mix, n_features, n_features)  if &quot;full&quot;</span></td>
      </tr>
      <tr>
        <td id="L588" class="blob-num js-line-number" data-line-number="588"></td>
        <td id="LC588" class="blob-code blob-code-inner js-file-line"><span class=pl-s>            (n_components, n_features, n_features)         if &quot;tied&quot;,</span></td>
      </tr>
      <tr>
        <td id="L589" class="blob-num js-line-number" data-line-number="589"></td>
        <td id="LC589" class="blob-code blob-code-inner js-file-line"><span class=pl-s>    &quot;&quot;&quot;</span></td>
      </tr>
      <tr>
        <td id="L590" class="blob-num js-line-number" data-line-number="590"></td>
        <td id="LC590" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L591" class="blob-num js-line-number" data-line-number="591"></td>
        <td id="LC591" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>__init__</span>(<span class=pl-s1>self</span>, <span class=pl-s1>n_components</span><span class=pl-c1>=</span><span class=pl-c1>1</span>, <span class=pl-s1>n_mix</span><span class=pl-c1>=</span><span class=pl-c1>1</span>,</td>
      </tr>
      <tr>
        <td id="L592" class="blob-num js-line-number" data-line-number="592"></td>
        <td id="LC592" class="blob-code blob-code-inner js-file-line">                 <span class=pl-s1>min_covar</span><span class=pl-c1>=</span><span class=pl-c1>1e-3</span>, <span class=pl-s1>startprob_prior</span><span class=pl-c1>=</span><span class=pl-c1>1.0</span>, <span class=pl-s1>transmat_prior</span><span class=pl-c1>=</span><span class=pl-c1>1.0</span>,</td>
      </tr>
      <tr>
        <td id="L593" class="blob-num js-line-number" data-line-number="593"></td>
        <td id="LC593" class="blob-code blob-code-inner js-file-line">                 <span class=pl-s1>weights_prior</span><span class=pl-c1>=</span><span class=pl-c1>1.0</span>, <span class=pl-s1>means_prior</span><span class=pl-c1>=</span><span class=pl-c1>0.0</span>, <span class=pl-s1>means_weight</span><span class=pl-c1>=</span><span class=pl-c1>0.0</span>,</td>
      </tr>
      <tr>
        <td id="L594" class="blob-num js-line-number" data-line-number="594"></td>
        <td id="LC594" class="blob-code blob-code-inner js-file-line">                 <span class=pl-s1>covars_prior</span><span class=pl-c1>=</span><span class=pl-c1>None</span>, <span class=pl-s1>covars_weight</span><span class=pl-c1>=</span><span class=pl-c1>None</span>,</td>
      </tr>
      <tr>
        <td id="L595" class="blob-num js-line-number" data-line-number="595"></td>
        <td id="LC595" class="blob-code blob-code-inner js-file-line">                 <span class=pl-s1>algorithm</span><span class=pl-c1>=</span><span class=pl-s>&quot;viterbi&quot;</span>, <span class=pl-s1>covariance_type</span><span class=pl-c1>=</span><span class=pl-s>&quot;diag&quot;</span>,</td>
      </tr>
      <tr>
        <td id="L596" class="blob-num js-line-number" data-line-number="596"></td>
        <td id="LC596" class="blob-code blob-code-inner js-file-line">                 <span class=pl-s1>random_state</span><span class=pl-c1>=</span><span class=pl-c1>None</span>, <span class=pl-s1>n_iter</span><span class=pl-c1>=</span><span class=pl-c1>10</span>, <span class=pl-s1>tol</span><span class=pl-c1>=</span><span class=pl-c1>1e-2</span>,</td>
      </tr>
      <tr>
        <td id="L597" class="blob-num js-line-number" data-line-number="597"></td>
        <td id="LC597" class="blob-code blob-code-inner js-file-line">                 <span class=pl-s1>verbose</span><span class=pl-c1>=</span><span class=pl-c1>False</span>, <span class=pl-s1>params</span><span class=pl-c1>=</span><span class=pl-s>&quot;stmcw&quot;</span>,</td>
      </tr>
      <tr>
        <td id="L598" class="blob-num js-line-number" data-line-number="598"></td>
        <td id="LC598" class="blob-code blob-code-inner js-file-line">                 <span class=pl-s1>init_params</span><span class=pl-c1>=</span><span class=pl-s>&quot;stmcw&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L599" class="blob-num js-line-number" data-line-number="599"></td>
        <td id="LC599" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>_BaseHMM</span>.<span class=pl-en>__init__</span>(<span class=pl-s1>self</span>, <span class=pl-s1>n_components</span>,</td>
      </tr>
      <tr>
        <td id="L600" class="blob-num js-line-number" data-line-number="600"></td>
        <td id="LC600" class="blob-code blob-code-inner js-file-line">                          <span class=pl-s1>startprob_prior</span><span class=pl-c1>=</span><span class=pl-s1>startprob_prior</span>,</td>
      </tr>
      <tr>
        <td id="L601" class="blob-num js-line-number" data-line-number="601"></td>
        <td id="LC601" class="blob-code blob-code-inner js-file-line">                          <span class=pl-s1>transmat_prior</span><span class=pl-c1>=</span><span class=pl-s1>transmat_prior</span>,</td>
      </tr>
      <tr>
        <td id="L602" class="blob-num js-line-number" data-line-number="602"></td>
        <td id="LC602" class="blob-code blob-code-inner js-file-line">                          <span class=pl-s1>algorithm</span><span class=pl-c1>=</span><span class=pl-s1>algorithm</span>, <span class=pl-s1>random_state</span><span class=pl-c1>=</span><span class=pl-s1>random_state</span>,</td>
      </tr>
      <tr>
        <td id="L603" class="blob-num js-line-number" data-line-number="603"></td>
        <td id="LC603" class="blob-code blob-code-inner js-file-line">                          <span class=pl-s1>n_iter</span><span class=pl-c1>=</span><span class=pl-s1>n_iter</span>, <span class=pl-s1>tol</span><span class=pl-c1>=</span><span class=pl-s1>tol</span>, <span class=pl-s1>verbose</span><span class=pl-c1>=</span><span class=pl-s1>verbose</span>,</td>
      </tr>
      <tr>
        <td id="L604" class="blob-num js-line-number" data-line-number="604"></td>
        <td id="LC604" class="blob-code blob-code-inner js-file-line">                          <span class=pl-s1>params</span><span class=pl-c1>=</span><span class=pl-s1>params</span>, <span class=pl-s1>init_params</span><span class=pl-c1>=</span><span class=pl-s1>init_params</span>)</td>
      </tr>
      <tr>
        <td id="L605" class="blob-num js-line-number" data-line-number="605"></td>
        <td id="LC605" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>=</span> <span class=pl-s1>covariance_type</span></td>
      </tr>
      <tr>
        <td id="L606" class="blob-num js-line-number" data-line-number="606"></td>
        <td id="LC606" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>min_covar</span> <span class=pl-c1>=</span> <span class=pl-s1>min_covar</span></td>
      </tr>
      <tr>
        <td id="L607" class="blob-num js-line-number" data-line-number="607"></td>
        <td id="LC607" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>n_mix</span> <span class=pl-c1>=</span> <span class=pl-s1>n_mix</span></td>
      </tr>
      <tr>
        <td id="L608" class="blob-num js-line-number" data-line-number="608"></td>
        <td id="LC608" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>weights_prior</span> <span class=pl-c1>=</span> <span class=pl-s1>weights_prior</span></td>
      </tr>
      <tr>
        <td id="L609" class="blob-num js-line-number" data-line-number="609"></td>
        <td id="LC609" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>means_prior</span> <span class=pl-c1>=</span> <span class=pl-s1>means_prior</span></td>
      </tr>
      <tr>
        <td id="L610" class="blob-num js-line-number" data-line-number="610"></td>
        <td id="LC610" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>means_weight</span> <span class=pl-c1>=</span> <span class=pl-s1>means_weight</span></td>
      </tr>
      <tr>
        <td id="L611" class="blob-num js-line-number" data-line-number="611"></td>
        <td id="LC611" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span> <span class=pl-c1>=</span> <span class=pl-s1>covars_prior</span></td>
      </tr>
      <tr>
        <td id="L612" class="blob-num js-line-number" data-line-number="612"></td>
        <td id="LC612" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span> <span class=pl-c1>=</span> <span class=pl-s1>covars_weight</span></td>
      </tr>
      <tr>
        <td id="L613" class="blob-num js-line-number" data-line-number="613"></td>
        <td id="LC613" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L614" class="blob-num js-line-number" data-line-number="614"></td>
        <td id="LC614" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_get_n_fit_scalars_per_param</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L615" class="blob-num js-line-number" data-line-number="615"></td>
        <td id="LC615" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>nc</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_components</span></td>
      </tr>
      <tr>
        <td id="L616" class="blob-num js-line-number" data-line-number="616"></td>
        <td id="LC616" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>nf</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span></td>
      </tr>
      <tr>
        <td id="L617" class="blob-num js-line-number" data-line-number="617"></td>
        <td id="LC617" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>nm</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_mix</span></td>
      </tr>
      <tr>
        <td id="L618" class="blob-num js-line-number" data-line-number="618"></td>
        <td id="LC618" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> {</td>
      </tr>
      <tr>
        <td id="L619" class="blob-num js-line-number" data-line-number="619"></td>
        <td id="LC619" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&quot;s&quot;</span>: <span class=pl-s1>nc</span> <span class=pl-c1>-</span> <span class=pl-c1>1</span>,</td>
      </tr>
      <tr>
        <td id="L620" class="blob-num js-line-number" data-line-number="620"></td>
        <td id="LC620" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&quot;t&quot;</span>: <span class=pl-s1>nc</span> <span class=pl-c1>*</span> (<span class=pl-s1>nc</span> <span class=pl-c1>-</span> <span class=pl-c1>1</span>),</td>
      </tr>
      <tr>
        <td id="L621" class="blob-num js-line-number" data-line-number="621"></td>
        <td id="LC621" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&quot;m&quot;</span>: <span class=pl-s1>nc</span> <span class=pl-c1>*</span> <span class=pl-s1>nm</span> <span class=pl-c1>*</span> <span class=pl-s1>nf</span>,</td>
      </tr>
      <tr>
        <td id="L622" class="blob-num js-line-number" data-line-number="622"></td>
        <td id="LC622" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&quot;c&quot;</span>: {</td>
      </tr>
      <tr>
        <td id="L623" class="blob-num js-line-number" data-line-number="623"></td>
        <td id="LC623" class="blob-code blob-code-inner js-file-line">                <span class=pl-s>&quot;spherical&quot;</span>: <span class=pl-s1>nc</span> <span class=pl-c1>*</span> <span class=pl-s1>nm</span>,</td>
      </tr>
      <tr>
        <td id="L624" class="blob-num js-line-number" data-line-number="624"></td>
        <td id="LC624" class="blob-code blob-code-inner js-file-line">                <span class=pl-s>&quot;diag&quot;</span>: <span class=pl-s1>nc</span> <span class=pl-c1>*</span> <span class=pl-s1>nm</span> <span class=pl-c1>*</span> <span class=pl-s1>nf</span>,</td>
      </tr>
      <tr>
        <td id="L625" class="blob-num js-line-number" data-line-number="625"></td>
        <td id="LC625" class="blob-code blob-code-inner js-file-line">                <span class=pl-s>&quot;full&quot;</span>: <span class=pl-s1>nc</span> <span class=pl-c1>*</span> <span class=pl-s1>nm</span> <span class=pl-c1>*</span> <span class=pl-s1>nf</span> <span class=pl-c1>*</span> (<span class=pl-s1>nf</span> <span class=pl-c1>+</span> <span class=pl-c1>1</span>) <span class=pl-c1>//</span> <span class=pl-c1>2</span>,</td>
      </tr>
      <tr>
        <td id="L626" class="blob-num js-line-number" data-line-number="626"></td>
        <td id="LC626" class="blob-code blob-code-inner js-file-line">                <span class=pl-s>&quot;tied&quot;</span>: <span class=pl-s1>nc</span> <span class=pl-c1>*</span> <span class=pl-s1>nf</span> <span class=pl-c1>*</span> (<span class=pl-s1>nf</span> <span class=pl-c1>+</span> <span class=pl-c1>1</span>) <span class=pl-c1>//</span> <span class=pl-c1>2</span>,</td>
      </tr>
      <tr>
        <td id="L627" class="blob-num js-line-number" data-line-number="627"></td>
        <td id="LC627" class="blob-code blob-code-inner js-file-line">            }[<span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span>],</td>
      </tr>
      <tr>
        <td id="L628" class="blob-num js-line-number" data-line-number="628"></td>
        <td id="LC628" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&quot;w&quot;</span>: <span class=pl-s1>nm</span> <span class=pl-c1>-</span> <span class=pl-c1>1</span>,</td>
      </tr>
      <tr>
        <td id="L629" class="blob-num js-line-number" data-line-number="629"></td>
        <td id="LC629" class="blob-code blob-code-inner js-file-line">        }</td>
      </tr>
      <tr>
        <td id="L630" class="blob-num js-line-number" data-line-number="630"></td>
        <td id="LC630" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L631" class="blob-num js-line-number" data-line-number="631"></td>
        <td id="LC631" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_init</span>(<span class=pl-s1>self</span>, <span class=pl-v>X</span>, <span class=pl-s1>lengths</span><span class=pl-c1>=</span><span class=pl-c1>None</span>):</td>
      </tr>
      <tr>
        <td id="L632" class="blob-num js-line-number" data-line-number="632"></td>
        <td id="LC632" class="blob-code blob-code-inner js-file-line">        <span class=pl-en>_check_and_set_gaussian_n_features</span>(<span class=pl-s1>self</span>, <span class=pl-v>X</span>)</td>
      </tr>
      <tr>
        <td id="L633" class="blob-num js-line-number" data-line-number="633"></td>
        <td id="LC633" class="blob-code blob-code-inner js-file-line">        <span class=pl-en>super</span>().<span class=pl-en>_init</span>(<span class=pl-v>X</span>, <span class=pl-s1>lengths</span><span class=pl-c1>=</span><span class=pl-s1>lengths</span>)</td>
      </tr>
      <tr>
        <td id="L634" class="blob-num js-line-number" data-line-number="634"></td>
        <td id="LC634" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>nc</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_components</span></td>
      </tr>
      <tr>
        <td id="L635" class="blob-num js-line-number" data-line-number="635"></td>
        <td id="LC635" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>nf</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span></td>
      </tr>
      <tr>
        <td id="L636" class="blob-num js-line-number" data-line-number="636"></td>
        <td id="LC636" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>nm</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_mix</span></td>
      </tr>
      <tr>
        <td id="L637" class="blob-num js-line-number" data-line-number="637"></td>
        <td id="LC637" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L638" class="blob-num js-line-number" data-line-number="638"></td>
        <td id="LC638" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Default values for covariance prior parameters</span></td>
      </tr>
      <tr>
        <td id="L639" class="blob-num js-line-number" data-line-number="639"></td>
        <td id="LC639" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-en>_init_covar_priors</span>()</td>
      </tr>
      <tr>
        <td id="L640" class="blob-num js-line-number" data-line-number="640"></td>
        <td id="LC640" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-en>_fix_priors_shape</span>()</td>
      </tr>
      <tr>
        <td id="L641" class="blob-num js-line-number" data-line-number="641"></td>
        <td id="LC641" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L642" class="blob-num js-line-number" data-line-number="642"></td>
        <td id="LC642" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>main_kmeans</span> <span class=pl-c1>=</span> <span class=pl-s1>cluster</span>.<span class=pl-v>KMeans</span>(<span class=pl-s1>n_clusters</span><span class=pl-c1>=</span><span class=pl-s1>nc</span>,</td>
      </tr>
      <tr>
        <td id="L643" class="blob-num js-line-number" data-line-number="643"></td>
        <td id="LC643" class="blob-code blob-code-inner js-file-line">                                     <span class=pl-s1>random_state</span><span class=pl-c1>=</span><span class=pl-s1>self</span>.<span class=pl-s1>random_state</span>)</td>
      </tr>
      <tr>
        <td id="L644" class="blob-num js-line-number" data-line-number="644"></td>
        <td id="LC644" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>labels</span> <span class=pl-c1>=</span> <span class=pl-s1>main_kmeans</span>.<span class=pl-en>fit_predict</span>(<span class=pl-v>X</span>)</td>
      </tr>
      <tr>
        <td id="L645" class="blob-num js-line-number" data-line-number="645"></td>
        <td id="LC645" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>kmeanses</span> <span class=pl-c1>=</span> []</td>
      </tr>
      <tr>
        <td id="L646" class="blob-num js-line-number" data-line-number="646"></td>
        <td id="LC646" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>for</span> <span class=pl-s1>label</span> <span class=pl-c1>in</span> <span class=pl-en>range</span>(<span class=pl-s1>nc</span>):</td>
      </tr>
      <tr>
        <td id="L647" class="blob-num js-line-number" data-line-number="647"></td>
        <td id="LC647" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>kmeans</span> <span class=pl-c1>=</span> <span class=pl-s1>cluster</span>.<span class=pl-v>KMeans</span>(<span class=pl-s1>n_clusters</span><span class=pl-c1>=</span><span class=pl-s1>nm</span>,</td>
      </tr>
      <tr>
        <td id="L648" class="blob-num js-line-number" data-line-number="648"></td>
        <td id="LC648" class="blob-code blob-code-inner js-file-line">                                    <span class=pl-s1>random_state</span><span class=pl-c1>=</span><span class=pl-s1>self</span>.<span class=pl-s1>random_state</span>)</td>
      </tr>
      <tr>
        <td id="L649" class="blob-num js-line-number" data-line-number="649"></td>
        <td id="LC649" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>kmeans</span>.<span class=pl-en>fit</span>(<span class=pl-v>X</span>[<span class=pl-s1>np</span>.<span class=pl-en>where</span>(<span class=pl-s1>labels</span> <span class=pl-c1>==</span> <span class=pl-s1>label</span>)])</td>
      </tr>
      <tr>
        <td id="L650" class="blob-num js-line-number" data-line-number="650"></td>
        <td id="LC650" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>kmeanses</span>.<span class=pl-en>append</span>(<span class=pl-s1>kmeans</span>)</td>
      </tr>
      <tr>
        <td id="L651" class="blob-num js-line-number" data-line-number="651"></td>
        <td id="LC651" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L652" class="blob-num js-line-number" data-line-number="652"></td>
        <td id="LC652" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s>&#39;w&#39;</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>init_params</span> <span class=pl-c1>or</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&quot;weights_&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L653" class="blob-num js-line-number" data-line-number="653"></td>
        <td id="LC653" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>weights_</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>ones</span>((<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>)) <span class=pl-c1>/</span> (<span class=pl-s1>np</span>.<span class=pl-en>ones</span>((<span class=pl-s1>nc</span>, <span class=pl-c1>1</span>)) <span class=pl-c1>*</span> <span class=pl-s1>nm</span>)</td>
      </tr>
      <tr>
        <td id="L654" class="blob-num js-line-number" data-line-number="654"></td>
        <td id="LC654" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L655" class="blob-num js-line-number" data-line-number="655"></td>
        <td id="LC655" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s>&#39;m&#39;</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>init_params</span> <span class=pl-c1>or</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&quot;means_&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L656" class="blob-num js-line-number" data-line-number="656"></td>
        <td id="LC656" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>means_</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>stack</span>(</td>
      </tr>
      <tr>
        <td id="L657" class="blob-num js-line-number" data-line-number="657"></td>
        <td id="LC657" class="blob-code blob-code-inner js-file-line">                [<span class=pl-s1>kmeans</span>.<span class=pl-s1>cluster_centers_</span> <span class=pl-k>for</span> <span class=pl-s1>kmeans</span> <span class=pl-c1>in</span> <span class=pl-s1>kmeanses</span>])</td>
      </tr>
      <tr>
        <td id="L658" class="blob-num js-line-number" data-line-number="658"></td>
        <td id="LC658" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L659" class="blob-num js-line-number" data-line-number="659"></td>
        <td id="LC659" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s>&#39;c&#39;</span> <span class=pl-c1>in</span> <span class=pl-s1>self</span>.<span class=pl-s1>init_params</span> <span class=pl-c1>or</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&quot;covars_&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L660" class="blob-num js-line-number" data-line-number="660"></td>
        <td id="LC660" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>cv</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>cov</span>(<span class=pl-v>X</span>.<span class=pl-v>T</span>) <span class=pl-c1>+</span> <span class=pl-s1>self</span>.<span class=pl-s1>min_covar</span> <span class=pl-c1>*</span> <span class=pl-s1>np</span>.<span class=pl-en>eye</span>(<span class=pl-s1>nf</span>)</td>
      </tr>
      <tr>
        <td id="L661" class="blob-num js-line-number" data-line-number="661"></td>
        <td id="LC661" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-s1>cv</span>.<span class=pl-s1>shape</span>:</td>
      </tr>
      <tr>
        <td id="L662" class="blob-num js-line-number" data-line-number="662"></td>
        <td id="LC662" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>cv</span>.<span class=pl-s1>shape</span> <span class=pl-c1>=</span> (<span class=pl-c1>1</span>, <span class=pl-c1>1</span>)</td>
      </tr>
      <tr>
        <td id="L663" class="blob-num js-line-number" data-line-number="663"></td>
        <td id="LC663" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;tied&#39;</span>:</td>
      </tr>
      <tr>
        <td id="L664" class="blob-num js-line-number" data-line-number="664"></td>
        <td id="LC664" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>zeros</span>((<span class=pl-s1>nc</span>, <span class=pl-s1>nf</span>, <span class=pl-s1>nf</span>))</td>
      </tr>
      <tr>
        <td id="L665" class="blob-num js-line-number" data-line-number="665"></td>
        <td id="LC665" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_</span>[:] <span class=pl-c1>=</span> <span class=pl-s1>cv</span></td>
      </tr>
      <tr>
        <td id="L666" class="blob-num js-line-number" data-line-number="666"></td>
        <td id="LC666" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>elif</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;full&#39;</span>:</td>
      </tr>
      <tr>
        <td id="L667" class="blob-num js-line-number" data-line-number="667"></td>
        <td id="LC667" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>zeros</span>((<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>, <span class=pl-s1>nf</span>, <span class=pl-s1>nf</span>))</td>
      </tr>
      <tr>
        <td id="L668" class="blob-num js-line-number" data-line-number="668"></td>
        <td id="LC668" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_</span>[:] <span class=pl-c1>=</span> <span class=pl-s1>cv</span></td>
      </tr>
      <tr>
        <td id="L669" class="blob-num js-line-number" data-line-number="669"></td>
        <td id="LC669" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>elif</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;diag&#39;</span>:</td>
      </tr>
      <tr>
        <td id="L670" class="blob-num js-line-number" data-line-number="670"></td>
        <td id="LC670" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>zeros</span>((<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>, <span class=pl-s1>nf</span>))</td>
      </tr>
      <tr>
        <td id="L671" class="blob-num js-line-number" data-line-number="671"></td>
        <td id="LC671" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_</span>[:] <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>diag</span>(<span class=pl-s1>cv</span>)</td>
      </tr>
      <tr>
        <td id="L672" class="blob-num js-line-number" data-line-number="672"></td>
        <td id="LC672" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>elif</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;spherical&#39;</span>:</td>
      </tr>
      <tr>
        <td id="L673" class="blob-num js-line-number" data-line-number="673"></td>
        <td id="LC673" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>zeros</span>((<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>))</td>
      </tr>
      <tr>
        <td id="L674" class="blob-num js-line-number" data-line-number="674"></td>
        <td id="LC674" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_</span>[:] <span class=pl-c1>=</span> <span class=pl-s1>cv</span>.<span class=pl-en>mean</span>()</td>
      </tr>
      <tr>
        <td id="L675" class="blob-num js-line-number" data-line-number="675"></td>
        <td id="LC675" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L676" class="blob-num js-line-number" data-line-number="676"></td>
        <td id="LC676" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_init_covar_priors</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L677" class="blob-num js-line-number" data-line-number="677"></td>
        <td id="LC677" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&quot;full&quot;</span>:</td>
      </tr>
      <tr>
        <td id="L678" class="blob-num js-line-number" data-line-number="678"></td>
        <td id="LC678" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span> <span class=pl-c1>is</span> <span class=pl-c1>None</span>:</td>
      </tr>
      <tr>
        <td id="L679" class="blob-num js-line-number" data-line-number="679"></td>
        <td id="LC679" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span> <span class=pl-c1>=</span> <span class=pl-c1>0.0</span></td>
      </tr>
      <tr>
        <td id="L680" class="blob-num js-line-number" data-line-number="680"></td>
        <td id="LC680" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span> <span class=pl-c1>is</span> <span class=pl-c1>None</span>:</td>
      </tr>
      <tr>
        <td id="L681" class="blob-num js-line-number" data-line-number="681"></td>
        <td id="LC681" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span> <span class=pl-c1>=</span> <span class=pl-c1>-</span>(<span class=pl-c1>1.0</span> <span class=pl-c1>+</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span> <span class=pl-c1>+</span> <span class=pl-c1>1.0</span>)</td>
      </tr>
      <tr>
        <td id="L682" class="blob-num js-line-number" data-line-number="682"></td>
        <td id="LC682" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>elif</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&quot;tied&quot;</span>:</td>
      </tr>
      <tr>
        <td id="L683" class="blob-num js-line-number" data-line-number="683"></td>
        <td id="LC683" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span> <span class=pl-c1>is</span> <span class=pl-c1>None</span>:</td>
      </tr>
      <tr>
        <td id="L684" class="blob-num js-line-number" data-line-number="684"></td>
        <td id="LC684" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span> <span class=pl-c1>=</span> <span class=pl-c1>0.0</span></td>
      </tr>
      <tr>
        <td id="L685" class="blob-num js-line-number" data-line-number="685"></td>
        <td id="LC685" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span> <span class=pl-c1>is</span> <span class=pl-c1>None</span>:</td>
      </tr>
      <tr>
        <td id="L686" class="blob-num js-line-number" data-line-number="686"></td>
        <td id="LC686" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span> <span class=pl-c1>=</span> <span class=pl-c1>-</span>(<span class=pl-s1>self</span>.<span class=pl-s1>n_mix</span> <span class=pl-c1>+</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span> <span class=pl-c1>+</span> <span class=pl-c1>1.0</span>)</td>
      </tr>
      <tr>
        <td id="L687" class="blob-num js-line-number" data-line-number="687"></td>
        <td id="LC687" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>elif</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&quot;diag&quot;</span>:</td>
      </tr>
      <tr>
        <td id="L688" class="blob-num js-line-number" data-line-number="688"></td>
        <td id="LC688" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span> <span class=pl-c1>is</span> <span class=pl-c1>None</span>:</td>
      </tr>
      <tr>
        <td id="L689" class="blob-num js-line-number" data-line-number="689"></td>
        <td id="LC689" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span> <span class=pl-c1>=</span> <span class=pl-c1>-</span><span class=pl-c1>1.5</span></td>
      </tr>
      <tr>
        <td id="L690" class="blob-num js-line-number" data-line-number="690"></td>
        <td id="LC690" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span> <span class=pl-c1>is</span> <span class=pl-c1>None</span>:</td>
      </tr>
      <tr>
        <td id="L691" class="blob-num js-line-number" data-line-number="691"></td>
        <td id="LC691" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span> <span class=pl-c1>=</span> <span class=pl-c1>0.0</span></td>
      </tr>
      <tr>
        <td id="L692" class="blob-num js-line-number" data-line-number="692"></td>
        <td id="LC692" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>elif</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&quot;spherical&quot;</span>:</td>
      </tr>
      <tr>
        <td id="L693" class="blob-num js-line-number" data-line-number="693"></td>
        <td id="LC693" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span> <span class=pl-c1>is</span> <span class=pl-c1>None</span>:</td>
      </tr>
      <tr>
        <td id="L694" class="blob-num js-line-number" data-line-number="694"></td>
        <td id="LC694" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span> <span class=pl-c1>=</span> <span class=pl-c1>-</span>(<span class=pl-s1>self</span>.<span class=pl-s1>n_mix</span> <span class=pl-c1>+</span> <span class=pl-c1>2.0</span>) <span class=pl-c1>/</span> <span class=pl-c1>2.0</span></td>
      </tr>
      <tr>
        <td id="L695" class="blob-num js-line-number" data-line-number="695"></td>
        <td id="LC695" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span> <span class=pl-c1>is</span> <span class=pl-c1>None</span>:</td>
      </tr>
      <tr>
        <td id="L696" class="blob-num js-line-number" data-line-number="696"></td>
        <td id="LC696" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span> <span class=pl-c1>=</span> <span class=pl-c1>0.0</span></td>
      </tr>
      <tr>
        <td id="L697" class="blob-num js-line-number" data-line-number="697"></td>
        <td id="LC697" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L698" class="blob-num js-line-number" data-line-number="698"></td>
        <td id="LC698" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_fix_priors_shape</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L699" class="blob-num js-line-number" data-line-number="699"></td>
        <td id="LC699" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>nc</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_components</span></td>
      </tr>
      <tr>
        <td id="L700" class="blob-num js-line-number" data-line-number="700"></td>
        <td id="LC700" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>nf</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span></td>
      </tr>
      <tr>
        <td id="L701" class="blob-num js-line-number" data-line-number="701"></td>
        <td id="LC701" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>nm</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_mix</span></td>
      </tr>
      <tr>
        <td id="L702" class="blob-num js-line-number" data-line-number="702"></td>
        <td id="LC702" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L703" class="blob-num js-line-number" data-line-number="703"></td>
        <td id="LC703" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># If priors are numbers, this function will make them into a</span></td>
      </tr>
      <tr>
        <td id="L704" class="blob-num js-line-number" data-line-number="704"></td>
        <td id="LC704" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># matrix of proper shape</span></td>
      </tr>
      <tr>
        <td id="L705" class="blob-num js-line-number" data-line-number="705"></td>
        <td id="LC705" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>weights_prior</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>broadcast_to</span>(</td>
      </tr>
      <tr>
        <td id="L706" class="blob-num js-line-number" data-line-number="706"></td>
        <td id="LC706" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>weights_prior</span>, (<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>)).<span class=pl-en>copy</span>()</td>
      </tr>
      <tr>
        <td id="L707" class="blob-num js-line-number" data-line-number="707"></td>
        <td id="LC707" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>means_prior</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>broadcast_to</span>(</td>
      </tr>
      <tr>
        <td id="L708" class="blob-num js-line-number" data-line-number="708"></td>
        <td id="LC708" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>means_prior</span>, (<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>, <span class=pl-s1>nf</span>)).<span class=pl-en>copy</span>()</td>
      </tr>
      <tr>
        <td id="L709" class="blob-num js-line-number" data-line-number="709"></td>
        <td id="LC709" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>means_weight</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>broadcast_to</span>(</td>
      </tr>
      <tr>
        <td id="L710" class="blob-num js-line-number" data-line-number="710"></td>
        <td id="LC710" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>means_weight</span>, (<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>)).<span class=pl-en>copy</span>()</td>
      </tr>
      <tr>
        <td id="L711" class="blob-num js-line-number" data-line-number="711"></td>
        <td id="LC711" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L712" class="blob-num js-line-number" data-line-number="712"></td>
        <td id="LC712" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&quot;full&quot;</span>:</td>
      </tr>
      <tr>
        <td id="L713" class="blob-num js-line-number" data-line-number="713"></td>
        <td id="LC713" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>broadcast_to</span>(</td>
      </tr>
      <tr>
        <td id="L714" class="blob-num js-line-number" data-line-number="714"></td>
        <td id="LC714" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span>, (<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>, <span class=pl-s1>nf</span>, <span class=pl-s1>nf</span>)).<span class=pl-en>copy</span>()</td>
      </tr>
      <tr>
        <td id="L715" class="blob-num js-line-number" data-line-number="715"></td>
        <td id="LC715" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>broadcast_to</span>(</td>
      </tr>
      <tr>
        <td id="L716" class="blob-num js-line-number" data-line-number="716"></td>
        <td id="LC716" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span>, (<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>)).<span class=pl-en>copy</span>()</td>
      </tr>
      <tr>
        <td id="L717" class="blob-num js-line-number" data-line-number="717"></td>
        <td id="LC717" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>elif</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&quot;tied&quot;</span>:</td>
      </tr>
      <tr>
        <td id="L718" class="blob-num js-line-number" data-line-number="718"></td>
        <td id="LC718" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>broadcast_to</span>(</td>
      </tr>
      <tr>
        <td id="L719" class="blob-num js-line-number" data-line-number="719"></td>
        <td id="LC719" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span>, (<span class=pl-s1>nc</span>, <span class=pl-s1>nf</span>, <span class=pl-s1>nf</span>)).<span class=pl-en>copy</span>()</td>
      </tr>
      <tr>
        <td id="L720" class="blob-num js-line-number" data-line-number="720"></td>
        <td id="LC720" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>broadcast_to</span>(</td>
      </tr>
      <tr>
        <td id="L721" class="blob-num js-line-number" data-line-number="721"></td>
        <td id="LC721" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span>, <span class=pl-s1>nc</span>).<span class=pl-en>copy</span>()</td>
      </tr>
      <tr>
        <td id="L722" class="blob-num js-line-number" data-line-number="722"></td>
        <td id="LC722" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>elif</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&quot;diag&quot;</span>:</td>
      </tr>
      <tr>
        <td id="L723" class="blob-num js-line-number" data-line-number="723"></td>
        <td id="LC723" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>broadcast_to</span>(</td>
      </tr>
      <tr>
        <td id="L724" class="blob-num js-line-number" data-line-number="724"></td>
        <td id="LC724" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span>, (<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>, <span class=pl-s1>nf</span>)).<span class=pl-en>copy</span>()</td>
      </tr>
      <tr>
        <td id="L725" class="blob-num js-line-number" data-line-number="725"></td>
        <td id="LC725" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>broadcast_to</span>(</td>
      </tr>
      <tr>
        <td id="L726" class="blob-num js-line-number" data-line-number="726"></td>
        <td id="LC726" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span>, (<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>, <span class=pl-s1>nf</span>)).<span class=pl-en>copy</span>()</td>
      </tr>
      <tr>
        <td id="L727" class="blob-num js-line-number" data-line-number="727"></td>
        <td id="LC727" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>elif</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&quot;spherical&quot;</span>:</td>
      </tr>
      <tr>
        <td id="L728" class="blob-num js-line-number" data-line-number="728"></td>
        <td id="LC728" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>broadcast_to</span>(</td>
      </tr>
      <tr>
        <td id="L729" class="blob-num js-line-number" data-line-number="729"></td>
        <td id="LC729" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span>, (<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>)).<span class=pl-en>copy</span>()</td>
      </tr>
      <tr>
        <td id="L730" class="blob-num js-line-number" data-line-number="730"></td>
        <td id="LC730" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>broadcast_to</span>(</td>
      </tr>
      <tr>
        <td id="L731" class="blob-num js-line-number" data-line-number="731"></td>
        <td id="LC731" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span>, (<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>)).<span class=pl-en>copy</span>()</td>
      </tr>
      <tr>
        <td id="L732" class="blob-num js-line-number" data-line-number="732"></td>
        <td id="LC732" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L733" class="blob-num js-line-number" data-line-number="733"></td>
        <td id="LC733" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_check</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L734" class="blob-num js-line-number" data-line-number="734"></td>
        <td id="LC734" class="blob-code blob-code-inner js-file-line">        <span class=pl-en>super</span>().<span class=pl-en>_check</span>()</td>
      </tr>
      <tr>
        <td id="L735" class="blob-num js-line-number" data-line-number="735"></td>
        <td id="LC735" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-en>hasattr</span>(<span class=pl-s1>self</span>, <span class=pl-s>&quot;n_features&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L736" class="blob-num js-line-number" data-line-number="736"></td>
        <td id="LC736" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>means_</span>.<span class=pl-s1>shape</span>[<span class=pl-c1>2</span>]</td>
      </tr>
      <tr>
        <td id="L737" class="blob-num js-line-number" data-line-number="737"></td>
        <td id="LC737" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>nc</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_components</span></td>
      </tr>
      <tr>
        <td id="L738" class="blob-num js-line-number" data-line-number="738"></td>
        <td id="LC738" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>nf</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span></td>
      </tr>
      <tr>
        <td id="L739" class="blob-num js-line-number" data-line-number="739"></td>
        <td id="LC739" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>nm</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_mix</span></td>
      </tr>
      <tr>
        <td id="L740" class="blob-num js-line-number" data-line-number="740"></td>
        <td id="LC740" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L741" class="blob-num js-line-number" data-line-number="741"></td>
        <td id="LC741" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-en>_init_covar_priors</span>()</td>
      </tr>
      <tr>
        <td id="L742" class="blob-num js-line-number" data-line-number="742"></td>
        <td id="LC742" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-en>_fix_priors_shape</span>()</td>
      </tr>
      <tr>
        <td id="L743" class="blob-num js-line-number" data-line-number="743"></td>
        <td id="LC743" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L744" class="blob-num js-line-number" data-line-number="744"></td>
        <td id="LC744" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Checking covariance type</span></td>
      </tr>
      <tr>
        <td id="L745" class="blob-num js-line-number" data-line-number="745"></td>
        <td id="LC745" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>not</span> <span class=pl-c1>in</span> <span class=pl-v>COVARIANCE_TYPES</span>:</td>
      </tr>
      <tr>
        <td id="L746" class="blob-num js-line-number" data-line-number="746"></td>
        <td id="LC746" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>raise</span> <span class=pl-v>ValueError</span>(<span class=pl-s>&quot;covariance_type must be one of {}&quot;</span></td>
      </tr>
      <tr>
        <td id="L747" class="blob-num js-line-number" data-line-number="747"></td>
        <td id="LC747" class="blob-code blob-code-inner js-file-line">                             .<span class=pl-en>format</span>(<span class=pl-v>COVARIANCE_TYPES</span>))</td>
      </tr>
      <tr>
        <td id="L748" class="blob-num js-line-number" data-line-number="748"></td>
        <td id="LC748" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L749" class="blob-num js-line-number" data-line-number="749"></td>
        <td id="LC749" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>weights_</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>array</span>(<span class=pl-s1>self</span>.<span class=pl-s1>weights_</span>)</td>
      </tr>
      <tr>
        <td id="L750" class="blob-num js-line-number" data-line-number="750"></td>
        <td id="LC750" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Checking mixture weights&#39; shape</span></td>
      </tr>
      <tr>
        <td id="L751" class="blob-num js-line-number" data-line-number="751"></td>
        <td id="LC751" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>weights_</span>.<span class=pl-s1>shape</span> <span class=pl-c1>!=</span> (<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>):</td>
      </tr>
      <tr>
        <td id="L752" class="blob-num js-line-number" data-line-number="752"></td>
        <td id="LC752" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>raise</span> <span class=pl-v>ValueError</span>(<span class=pl-s>&quot;mixture weights must have shape &quot;</span></td>
      </tr>
      <tr>
        <td id="L753" class="blob-num js-line-number" data-line-number="753"></td>
        <td id="LC753" class="blob-code blob-code-inner js-file-line">                             <span class=pl-s>&quot;(n_components, n_mix), actual shape: {}&quot;</span></td>
      </tr>
      <tr>
        <td id="L754" class="blob-num js-line-number" data-line-number="754"></td>
        <td id="LC754" class="blob-code blob-code-inner js-file-line">                             .<span class=pl-en>format</span>(<span class=pl-s1>self</span>.<span class=pl-s1>weights_</span>.<span class=pl-s1>shape</span>))</td>
      </tr>
      <tr>
        <td id="L755" class="blob-num js-line-number" data-line-number="755"></td>
        <td id="LC755" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L756" class="blob-num js-line-number" data-line-number="756"></td>
        <td id="LC756" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Checking mixture weights&#39; mathematical correctness</span></td>
      </tr>
      <tr>
        <td id="L757" class="blob-num js-line-number" data-line-number="757"></td>
        <td id="LC757" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-s1>np</span>.<span class=pl-en>allclose</span>(<span class=pl-s1>np</span>.<span class=pl-en>sum</span>(<span class=pl-s1>self</span>.<span class=pl-s1>weights_</span>, <span class=pl-s1>axis</span><span class=pl-c1>=</span><span class=pl-c1>1</span>), <span class=pl-s1>np</span>.<span class=pl-en>ones</span>(<span class=pl-s1>nc</span>)):</td>
      </tr>
      <tr>
        <td id="L758" class="blob-num js-line-number" data-line-number="758"></td>
        <td id="LC758" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>raise</span> <span class=pl-v>ValueError</span>(<span class=pl-s>&quot;mixture weights must sum up to 1&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L759" class="blob-num js-line-number" data-line-number="759"></td>
        <td id="LC759" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L760" class="blob-num js-line-number" data-line-number="760"></td>
        <td id="LC760" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Checking means&#39; shape</span></td>
      </tr>
      <tr>
        <td id="L761" class="blob-num js-line-number" data-line-number="761"></td>
        <td id="LC761" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>means_</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>array</span>(<span class=pl-s1>self</span>.<span class=pl-s1>means_</span>)</td>
      </tr>
      <tr>
        <td id="L762" class="blob-num js-line-number" data-line-number="762"></td>
        <td id="LC762" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>means_</span>.<span class=pl-s1>shape</span> <span class=pl-c1>!=</span> (<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>, <span class=pl-s1>nf</span>):</td>
      </tr>
      <tr>
        <td id="L763" class="blob-num js-line-number" data-line-number="763"></td>
        <td id="LC763" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>raise</span> <span class=pl-v>ValueError</span>(<span class=pl-s>&quot;mixture means must have shape &quot;</span></td>
      </tr>
      <tr>
        <td id="L764" class="blob-num js-line-number" data-line-number="764"></td>
        <td id="LC764" class="blob-code blob-code-inner js-file-line">                             <span class=pl-s>&quot;(n_components, n_mix, n_features), &quot;</span></td>
      </tr>
      <tr>
        <td id="L765" class="blob-num js-line-number" data-line-number="765"></td>
        <td id="LC765" class="blob-code blob-code-inner js-file-line">                             <span class=pl-s>&quot;actual shape: {}&quot;</span>.<span class=pl-en>format</span>(<span class=pl-s1>self</span>.<span class=pl-s1>means_</span>.<span class=pl-s1>shape</span>))</td>
      </tr>
      <tr>
        <td id="L766" class="blob-num js-line-number" data-line-number="766"></td>
        <td id="LC766" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L767" class="blob-num js-line-number" data-line-number="767"></td>
        <td id="LC767" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Checking covariances&#39; shape</span></td>
      </tr>
      <tr>
        <td id="L768" class="blob-num js-line-number" data-line-number="768"></td>
        <td id="LC768" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>covars_</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>array</span>(<span class=pl-s1>self</span>.<span class=pl-s1>covars_</span>)</td>
      </tr>
      <tr>
        <td id="L769" class="blob-num js-line-number" data-line-number="769"></td>
        <td id="LC769" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>covars_shape</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>covars_</span>.<span class=pl-s1>shape</span></td>
      </tr>
      <tr>
        <td id="L770" class="blob-num js-line-number" data-line-number="770"></td>
        <td id="LC770" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>needed_shapes</span> <span class=pl-c1>=</span> {</td>
      </tr>
      <tr>
        <td id="L771" class="blob-num js-line-number" data-line-number="771"></td>
        <td id="LC771" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&quot;spherical&quot;</span>: (<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>),</td>
      </tr>
      <tr>
        <td id="L772" class="blob-num js-line-number" data-line-number="772"></td>
        <td id="LC772" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&quot;tied&quot;</span>: (<span class=pl-s1>nc</span>, <span class=pl-s1>nf</span>, <span class=pl-s1>nf</span>),</td>
      </tr>
      <tr>
        <td id="L773" class="blob-num js-line-number" data-line-number="773"></td>
        <td id="LC773" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&quot;diag&quot;</span>: (<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>, <span class=pl-s1>nf</span>),</td>
      </tr>
      <tr>
        <td id="L774" class="blob-num js-line-number" data-line-number="774"></td>
        <td id="LC774" class="blob-code blob-code-inner js-file-line">            <span class=pl-s>&quot;full&quot;</span>: (<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>, <span class=pl-s1>nf</span>, <span class=pl-s1>nf</span>),</td>
      </tr>
      <tr>
        <td id="L775" class="blob-num js-line-number" data-line-number="775"></td>
        <td id="LC775" class="blob-code blob-code-inner js-file-line">        }</td>
      </tr>
      <tr>
        <td id="L776" class="blob-num js-line-number" data-line-number="776"></td>
        <td id="LC776" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>needed_shape</span> <span class=pl-c1>=</span> <span class=pl-s1>needed_shapes</span>[<span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span>]</td>
      </tr>
      <tr>
        <td id="L777" class="blob-num js-line-number" data-line-number="777"></td>
        <td id="LC777" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>covars_shape</span> <span class=pl-c1>!=</span> <span class=pl-s1>needed_shape</span>:</td>
      </tr>
      <tr>
        <td id="L778" class="blob-num js-line-number" data-line-number="778"></td>
        <td id="LC778" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>raise</span> <span class=pl-v>ValueError</span>(<span class=pl-s>&quot;{!r} mixture covars must have shape {}, &quot;</span></td>
      </tr>
      <tr>
        <td id="L779" class="blob-num js-line-number" data-line-number="779"></td>
        <td id="LC779" class="blob-code blob-code-inner js-file-line">                             <span class=pl-s>&quot;actual shape: {}&quot;</span></td>
      </tr>
      <tr>
        <td id="L780" class="blob-num js-line-number" data-line-number="780"></td>
        <td id="LC780" class="blob-code blob-code-inner js-file-line">                             .<span class=pl-en>format</span>(<span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span>,</td>
      </tr>
      <tr>
        <td id="L781" class="blob-num js-line-number" data-line-number="781"></td>
        <td id="LC781" class="blob-code blob-code-inner js-file-line">                                     <span class=pl-s1>needed_shape</span>, <span class=pl-s1>covars_shape</span>))</td>
      </tr>
      <tr>
        <td id="L782" class="blob-num js-line-number" data-line-number="782"></td>
        <td id="LC782" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L783" class="blob-num js-line-number" data-line-number="783"></td>
        <td id="LC783" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Checking covariances&#39; mathematical correctness</span></td>
      </tr>
      <tr>
        <td id="L784" class="blob-num js-line-number" data-line-number="784"></td>
        <td id="LC784" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>from</span> <span class=pl-s1>scipy</span> <span class=pl-k>import</span> <span class=pl-s1>linalg</span></td>
      </tr>
      <tr>
        <td id="L785" class="blob-num js-line-number" data-line-number="785"></td>
        <td id="LC785" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L786" class="blob-num js-line-number" data-line-number="786"></td>
        <td id="LC786" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> (<span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&quot;spherical&quot;</span> <span class=pl-c1>or</span></td>
      </tr>
      <tr>
        <td id="L787" class="blob-num js-line-number" data-line-number="787"></td>
        <td id="LC787" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&quot;diag&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L788" class="blob-num js-line-number" data-line-number="788"></td>
        <td id="LC788" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>np</span>.<span class=pl-en>any</span>(<span class=pl-s1>self</span>.<span class=pl-s1>covars_</span> <span class=pl-c1>&lt;</span> <span class=pl-c1>0</span>):</td>
      </tr>
      <tr>
        <td id="L789" class="blob-num js-line-number" data-line-number="789"></td>
        <td id="LC789" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>raise</span> <span class=pl-v>ValueError</span>(<span class=pl-s>&quot;{!r} mixture covars must be non-negative&quot;</span></td>
      </tr>
      <tr>
        <td id="L790" class="blob-num js-line-number" data-line-number="790"></td>
        <td id="LC790" class="blob-code blob-code-inner js-file-line">                                 .<span class=pl-en>format</span>(<span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span>))</td>
      </tr>
      <tr>
        <td id="L791" class="blob-num js-line-number" data-line-number="791"></td>
        <td id="LC791" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>if</span> <span class=pl-s1>np</span>.<span class=pl-en>any</span>(<span class=pl-s1>self</span>.<span class=pl-s1>covars_</span> <span class=pl-c1>==</span> <span class=pl-c1>0</span>):</td>
      </tr>
      <tr>
        <td id="L792" class="blob-num js-line-number" data-line-number="792"></td>
        <td id="LC792" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>_log</span>.<span class=pl-en>warning</span>(<span class=pl-s>&quot;Degenerate mixture covariance&quot;</span>)</td>
      </tr>
      <tr>
        <td id="L793" class="blob-num js-line-number" data-line-number="793"></td>
        <td id="LC793" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>elif</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&quot;tied&quot;</span>:</td>
      </tr>
      <tr>
        <td id="L794" class="blob-num js-line-number" data-line-number="794"></td>
        <td id="LC794" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>i</span>, <span class=pl-s1>covar</span> <span class=pl-c1>in</span> <span class=pl-en>enumerate</span>(<span class=pl-s1>self</span>.<span class=pl-s1>covars_</span>):</td>
      </tr>
      <tr>
        <td id="L795" class="blob-num js-line-number" data-line-number="795"></td>
        <td id="LC795" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-s1>np</span>.<span class=pl-en>allclose</span>(<span class=pl-s1>covar</span>, <span class=pl-s1>covar</span>.<span class=pl-v>T</span>):</td>
      </tr>
      <tr>
        <td id="L796" class="blob-num js-line-number" data-line-number="796"></td>
        <td id="LC796" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>raise</span> <span class=pl-v>ValueError</span>(<span class=pl-s>&quot;Covariance of state #{} is not symmetric&quot;</span></td>
      </tr>
      <tr>
        <td id="L797" class="blob-num js-line-number" data-line-number="797"></td>
        <td id="LC797" class="blob-code blob-code-inner js-file-line">                                     .<span class=pl-en>format</span>(<span class=pl-s1>i</span>))</td>
      </tr>
      <tr>
        <td id="L798" class="blob-num js-line-number" data-line-number="798"></td>
        <td id="LC798" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>min_eigvalsh</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-s1>linalg</span>.<span class=pl-en>eigvalsh</span>(<span class=pl-s1>covar</span>).<span class=pl-en>min</span>()</td>
      </tr>
      <tr>
        <td id="L799" class="blob-num js-line-number" data-line-number="799"></td>
        <td id="LC799" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-s1>min_eigvalsh</span> <span class=pl-c1>&lt;</span> <span class=pl-c1>0</span>:</td>
      </tr>
      <tr>
        <td id="L800" class="blob-num js-line-number" data-line-number="800"></td>
        <td id="LC800" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>raise</span> <span class=pl-v>ValueError</span>(<span class=pl-s>&quot;Covariance of state #{} is not positive &quot;</span></td>
      </tr>
      <tr>
        <td id="L801" class="blob-num js-line-number" data-line-number="801"></td>
        <td id="LC801" class="blob-code blob-code-inner js-file-line">                                     <span class=pl-s>&quot;definite&quot;</span>.<span class=pl-en>format</span>(<span class=pl-s1>i</span>))</td>
      </tr>
      <tr>
        <td id="L802" class="blob-num js-line-number" data-line-number="802"></td>
        <td id="LC802" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>if</span> <span class=pl-s1>min_eigvalsh</span> <span class=pl-c1>==</span> <span class=pl-c1>0</span>:</td>
      </tr>
      <tr>
        <td id="L803" class="blob-num js-line-number" data-line-number="803"></td>
        <td id="LC803" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>_log</span>.<span class=pl-en>warning</span>(<span class=pl-s>&quot;Covariance of state #%d has a null &quot;</span></td>
      </tr>
      <tr>
        <td id="L804" class="blob-num js-line-number" data-line-number="804"></td>
        <td id="LC804" class="blob-code blob-code-inner js-file-line">                                 <span class=pl-s>&quot;eigenvalue.&quot;</span>, <span class=pl-s1>i</span>)</td>
      </tr>
      <tr>
        <td id="L805" class="blob-num js-line-number" data-line-number="805"></td>
        <td id="LC805" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>elif</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&quot;full&quot;</span>:</td>
      </tr>
      <tr>
        <td id="L806" class="blob-num js-line-number" data-line-number="806"></td>
        <td id="LC806" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>for</span> <span class=pl-s1>i</span>, <span class=pl-s1>mix_covars</span> <span class=pl-c1>in</span> <span class=pl-en>enumerate</span>(<span class=pl-s1>self</span>.<span class=pl-s1>covars_</span>):</td>
      </tr>
      <tr>
        <td id="L807" class="blob-num js-line-number" data-line-number="807"></td>
        <td id="LC807" class="blob-code blob-code-inner js-file-line">                <span class=pl-k>for</span> <span class=pl-s1>j</span>, <span class=pl-s1>covar</span> <span class=pl-c1>in</span> <span class=pl-en>enumerate</span>(<span class=pl-s1>mix_covars</span>):</td>
      </tr>
      <tr>
        <td id="L808" class="blob-num js-line-number" data-line-number="808"></td>
        <td id="LC808" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>if</span> <span class=pl-c1>not</span> <span class=pl-s1>np</span>.<span class=pl-en>allclose</span>(<span class=pl-s1>covar</span>, <span class=pl-s1>covar</span>.<span class=pl-v>T</span>):</td>
      </tr>
      <tr>
        <td id="L809" class="blob-num js-line-number" data-line-number="809"></td>
        <td id="LC809" class="blob-code blob-code-inner js-file-line">                        <span class=pl-k>raise</span> <span class=pl-v>ValueError</span>(</td>
      </tr>
      <tr>
        <td id="L810" class="blob-num js-line-number" data-line-number="810"></td>
        <td id="LC810" class="blob-code blob-code-inner js-file-line">                            <span class=pl-s>&quot;Covariance of state #{}, mixture #{} is not &quot;</span></td>
      </tr>
      <tr>
        <td id="L811" class="blob-num js-line-number" data-line-number="811"></td>
        <td id="LC811" class="blob-code blob-code-inner js-file-line">                            <span class=pl-s>&quot;symmetric&quot;</span>.<span class=pl-en>format</span>(<span class=pl-s1>i</span>, <span class=pl-s1>j</span>))</td>
      </tr>
      <tr>
        <td id="L812" class="blob-num js-line-number" data-line-number="812"></td>
        <td id="LC812" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s1>min_eigvalsh</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-s1>linalg</span>.<span class=pl-en>eigvalsh</span>(<span class=pl-s1>covar</span>).<span class=pl-en>min</span>()</td>
      </tr>
      <tr>
        <td id="L813" class="blob-num js-line-number" data-line-number="813"></td>
        <td id="LC813" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>if</span> <span class=pl-s1>min_eigvalsh</span> <span class=pl-c1>&lt;</span> <span class=pl-c1>0</span>:</td>
      </tr>
      <tr>
        <td id="L814" class="blob-num js-line-number" data-line-number="814"></td>
        <td id="LC814" class="blob-code blob-code-inner js-file-line">                        <span class=pl-k>raise</span> <span class=pl-v>ValueError</span>(</td>
      </tr>
      <tr>
        <td id="L815" class="blob-num js-line-number" data-line-number="815"></td>
        <td id="LC815" class="blob-code blob-code-inner js-file-line">                            <span class=pl-s>&quot;Covariance of state #{}, mixture #{} is not &quot;</span></td>
      </tr>
      <tr>
        <td id="L816" class="blob-num js-line-number" data-line-number="816"></td>
        <td id="LC816" class="blob-code blob-code-inner js-file-line">                            <span class=pl-s>&quot;positive definite&quot;</span>.<span class=pl-en>format</span>(<span class=pl-s1>i</span>, <span class=pl-s1>j</span>))</td>
      </tr>
      <tr>
        <td id="L817" class="blob-num js-line-number" data-line-number="817"></td>
        <td id="LC817" class="blob-code blob-code-inner js-file-line">                    <span class=pl-k>if</span> <span class=pl-s1>min_eigvalsh</span> <span class=pl-c1>==</span> <span class=pl-c1>0</span>:</td>
      </tr>
      <tr>
        <td id="L818" class="blob-num js-line-number" data-line-number="818"></td>
        <td id="LC818" class="blob-code blob-code-inner js-file-line">                        <span class=pl-s1>_log</span>.<span class=pl-en>warning</span>(<span class=pl-s>&quot;Covariance of state #%d, mixture #%d &quot;</span></td>
      </tr>
      <tr>
        <td id="L819" class="blob-num js-line-number" data-line-number="819"></td>
        <td id="LC819" class="blob-code blob-code-inner js-file-line">                                     <span class=pl-s>&quot;has a null eigenvalue.&quot;</span>, <span class=pl-s1>i</span>, <span class=pl-s1>j</span>)</td>
      </tr>
      <tr>
        <td id="L820" class="blob-num js-line-number" data-line-number="820"></td>
        <td id="LC820" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L821" class="blob-num js-line-number" data-line-number="821"></td>
        <td id="LC821" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_generate_sample_from_state</span>(<span class=pl-s1>self</span>, <span class=pl-s1>state</span>, <span class=pl-s1>random_state</span><span class=pl-c1>=</span><span class=pl-c1>None</span>):</td>
      </tr>
      <tr>
        <td id="L822" class="blob-num js-line-number" data-line-number="822"></td>
        <td id="LC822" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>random_state</span> <span class=pl-c1>is</span> <span class=pl-c1>None</span>:</td>
      </tr>
      <tr>
        <td id="L823" class="blob-num js-line-number" data-line-number="823"></td>
        <td id="LC823" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>random_state</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>random_state</span></td>
      </tr>
      <tr>
        <td id="L824" class="blob-num js-line-number" data-line-number="824"></td>
        <td id="LC824" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>random_state</span> <span class=pl-c1>=</span> <span class=pl-en>check_random_state</span>(<span class=pl-s1>random_state</span>)</td>
      </tr>
      <tr>
        <td id="L825" class="blob-num js-line-number" data-line-number="825"></td>
        <td id="LC825" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L826" class="blob-num js-line-number" data-line-number="826"></td>
        <td id="LC826" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>cur_weights</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>weights_</span>[<span class=pl-s1>state</span>]</td>
      </tr>
      <tr>
        <td id="L827" class="blob-num js-line-number" data-line-number="827"></td>
        <td id="LC827" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>i_gauss</span> <span class=pl-c1>=</span> <span class=pl-s1>random_state</span>.<span class=pl-en>choice</span>(<span class=pl-s1>self</span>.<span class=pl-s1>n_mix</span>, <span class=pl-s1>p</span><span class=pl-c1>=</span><span class=pl-s1>cur_weights</span>)</td>
      </tr>
      <tr>
        <td id="L828" class="blob-num js-line-number" data-line-number="828"></td>
        <td id="LC828" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;tied&#39;</span>:</td>
      </tr>
      <tr>
        <td id="L829" class="blob-num js-line-number" data-line-number="829"></td>
        <td id="LC829" class="blob-code blob-code-inner js-file-line">            <span class=pl-c># self.covars_.shape == (n_components, n_features, n_features)</span></td>
      </tr>
      <tr>
        <td id="L830" class="blob-num js-line-number" data-line-number="830"></td>
        <td id="LC830" class="blob-code blob-code-inner js-file-line">            <span class=pl-c># shouldn&#39;t that be (n_mix, ...)?</span></td>
      </tr>
      <tr>
        <td id="L831" class="blob-num js-line-number" data-line-number="831"></td>
        <td id="LC831" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>covs</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>covars_</span></td>
      </tr>
      <tr>
        <td id="L832" class="blob-num js-line-number" data-line-number="832"></td>
        <td id="LC832" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>else</span>:</td>
      </tr>
      <tr>
        <td id="L833" class="blob-num js-line-number" data-line-number="833"></td>
        <td id="LC833" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>covs</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>covars_</span>[:, <span class=pl-s1>i_gauss</span>]</td>
      </tr>
      <tr>
        <td id="L834" class="blob-num js-line-number" data-line-number="834"></td>
        <td id="LC834" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>covs</span> <span class=pl-c1>=</span> <span class=pl-en>fill_covars</span>(<span class=pl-s1>covs</span>, <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span>,</td>
      </tr>
      <tr>
        <td id="L835" class="blob-num js-line-number" data-line-number="835"></td>
        <td id="LC835" class="blob-code blob-code-inner js-file-line">                               <span class=pl-s1>self</span>.<span class=pl-s1>n_components</span>, <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span>)</td>
      </tr>
      <tr>
        <td id="L836" class="blob-num js-line-number" data-line-number="836"></td>
        <td id="LC836" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>random_state</span>.<span class=pl-en>multivariate_normal</span>(</td>
      </tr>
      <tr>
        <td id="L837" class="blob-num js-line-number" data-line-number="837"></td>
        <td id="LC837" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>self</span>.<span class=pl-s1>means_</span>[<span class=pl-s1>state</span>, <span class=pl-s1>i_gauss</span>], <span class=pl-s1>covs</span>[<span class=pl-s1>state</span>]</td>
      </tr>
      <tr>
        <td id="L838" class="blob-num js-line-number" data-line-number="838"></td>
        <td id="LC838" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L839" class="blob-num js-line-number" data-line-number="839"></td>
        <td id="LC839" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L840" class="blob-num js-line-number" data-line-number="840"></td>
        <td id="LC840" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_compute_log_weighted_gaussian_densities</span>(<span class=pl-s1>self</span>, <span class=pl-v>X</span>, <span class=pl-s1>i_comp</span>):</td>
      </tr>
      <tr>
        <td id="L841" class="blob-num js-line-number" data-line-number="841"></td>
        <td id="LC841" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>cur_means</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>means_</span>[<span class=pl-s1>i_comp</span>]</td>
      </tr>
      <tr>
        <td id="L842" class="blob-num js-line-number" data-line-number="842"></td>
        <td id="LC842" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>cur_covs</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>covars_</span>[<span class=pl-s1>i_comp</span>]</td>
      </tr>
      <tr>
        <td id="L843" class="blob-num js-line-number" data-line-number="843"></td>
        <td id="LC843" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;spherical&#39;</span>:</td>
      </tr>
      <tr>
        <td id="L844" class="blob-num js-line-number" data-line-number="844"></td>
        <td id="LC844" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>cur_covs</span> <span class=pl-c1>=</span> <span class=pl-s1>cur_covs</span>[:, <span class=pl-s1>np</span>.<span class=pl-s1>newaxis</span>]</td>
      </tr>
      <tr>
        <td id="L845" class="blob-num js-line-number" data-line-number="845"></td>
        <td id="LC845" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>log_cur_weights</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>log</span>(<span class=pl-s1>self</span>.<span class=pl-s1>weights_</span>[<span class=pl-s1>i_comp</span>])</td>
      </tr>
      <tr>
        <td id="L846" class="blob-num js-line-number" data-line-number="846"></td>
        <td id="LC846" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L847" class="blob-num js-line-number" data-line-number="847"></td>
        <td id="LC847" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-en>log_multivariate_normal_density</span>(</td>
      </tr>
      <tr>
        <td id="L848" class="blob-num js-line-number" data-line-number="848"></td>
        <td id="LC848" class="blob-code blob-code-inner js-file-line">            <span class=pl-v>X</span>, <span class=pl-s1>cur_means</span>, <span class=pl-s1>cur_covs</span>, <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span></td>
      </tr>
      <tr>
        <td id="L849" class="blob-num js-line-number" data-line-number="849"></td>
        <td id="LC849" class="blob-code blob-code-inner js-file-line">        ) <span class=pl-c1>+</span> <span class=pl-s1>log_cur_weights</span></td>
      </tr>
      <tr>
        <td id="L850" class="blob-num js-line-number" data-line-number="850"></td>
        <td id="LC850" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L851" class="blob-num js-line-number" data-line-number="851"></td>
        <td id="LC851" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_compute_log_likelihood</span>(<span class=pl-s1>self</span>, <span class=pl-v>X</span>):</td>
      </tr>
      <tr>
        <td id="L852" class="blob-num js-line-number" data-line-number="852"></td>
        <td id="LC852" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>n_samples</span>, <span class=pl-s1>_</span> <span class=pl-c1>=</span> <span class=pl-v>X</span>.<span class=pl-s1>shape</span></td>
      </tr>
      <tr>
        <td id="L853" class="blob-num js-line-number" data-line-number="853"></td>
        <td id="LC853" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>res</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>zeros</span>((<span class=pl-s1>n_samples</span>, <span class=pl-s1>self</span>.<span class=pl-s1>n_components</span>))</td>
      </tr>
      <tr>
        <td id="L854" class="blob-num js-line-number" data-line-number="854"></td>
        <td id="LC854" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L855" class="blob-num js-line-number" data-line-number="855"></td>
        <td id="LC855" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>for</span> <span class=pl-s1>i</span> <span class=pl-c1>in</span> <span class=pl-en>range</span>(<span class=pl-s1>self</span>.<span class=pl-s1>n_components</span>):</td>
      </tr>
      <tr>
        <td id="L856" class="blob-num js-line-number" data-line-number="856"></td>
        <td id="LC856" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>log_denses</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-en>_compute_log_weighted_gaussian_densities</span>(<span class=pl-v>X</span>, <span class=pl-s1>i</span>)</td>
      </tr>
      <tr>
        <td id="L857" class="blob-num js-line-number" data-line-number="857"></td>
        <td id="LC857" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>with</span> <span class=pl-s1>np</span>.<span class=pl-en>errstate</span>(<span class=pl-s1>under</span><span class=pl-c1>=</span><span class=pl-s>&quot;ignore&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L858" class="blob-num js-line-number" data-line-number="858"></td>
        <td id="LC858" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>res</span>[:, <span class=pl-s1>i</span>] <span class=pl-c1>=</span> <span class=pl-en>logsumexp</span>(<span class=pl-s1>log_denses</span>, <span class=pl-s1>axis</span><span class=pl-c1>=</span><span class=pl-c1>1</span>)</td>
      </tr>
      <tr>
        <td id="L859" class="blob-num js-line-number" data-line-number="859"></td>
        <td id="LC859" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L860" class="blob-num js-line-number" data-line-number="860"></td>
        <td id="LC860" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>res</span></td>
      </tr>
      <tr>
        <td id="L861" class="blob-num js-line-number" data-line-number="861"></td>
        <td id="LC861" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L862" class="blob-num js-line-number" data-line-number="862"></td>
        <td id="LC862" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_initialize_sufficient_statistics</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L863" class="blob-num js-line-number" data-line-number="863"></td>
        <td id="LC863" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>stats</span> <span class=pl-c1>=</span> <span class=pl-en>super</span>().<span class=pl-en>_initialize_sufficient_statistics</span>()</td>
      </tr>
      <tr>
        <td id="L864" class="blob-num js-line-number" data-line-number="864"></td>
        <td id="LC864" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>stats</span>[<span class=pl-s>&#39;n_samples&#39;</span>] <span class=pl-c1>=</span> <span class=pl-c1>0</span></td>
      </tr>
      <tr>
        <td id="L865" class="blob-num js-line-number" data-line-number="865"></td>
        <td id="LC865" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post_comp_mix&#39;</span>] <span class=pl-c1>=</span> <span class=pl-c1>None</span></td>
      </tr>
      <tr>
        <td id="L866" class="blob-num js-line-number" data-line-number="866"></td>
        <td id="LC866" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post_mix_sum&#39;</span>] <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>zeros</span>((<span class=pl-s1>self</span>.<span class=pl-s1>n_components</span>, <span class=pl-s1>self</span>.<span class=pl-s1>n_mix</span>))</td>
      </tr>
      <tr>
        <td id="L867" class="blob-num js-line-number" data-line-number="867"></td>
        <td id="LC867" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post_sum&#39;</span>] <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>zeros</span>(<span class=pl-s1>self</span>.<span class=pl-s1>n_components</span>)</td>
      </tr>
      <tr>
        <td id="L868" class="blob-num js-line-number" data-line-number="868"></td>
        <td id="LC868" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>stats</span>[<span class=pl-s>&#39;samples&#39;</span>] <span class=pl-c1>=</span> <span class=pl-c1>None</span></td>
      </tr>
      <tr>
        <td id="L869" class="blob-num js-line-number" data-line-number="869"></td>
        <td id="LC869" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>stats</span>[<span class=pl-s>&#39;centered&#39;</span>] <span class=pl-c1>=</span> <span class=pl-c1>None</span></td>
      </tr>
      <tr>
        <td id="L870" class="blob-num js-line-number" data-line-number="870"></td>
        <td id="LC870" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>return</span> <span class=pl-s1>stats</span></td>
      </tr>
      <tr>
        <td id="L871" class="blob-num js-line-number" data-line-number="871"></td>
        <td id="LC871" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L872" class="blob-num js-line-number" data-line-number="872"></td>
        <td id="LC872" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_accumulate_sufficient_statistics</span>(<span class=pl-s1>self</span>, <span class=pl-s1>stats</span>, <span class=pl-v>X</span>, <span class=pl-s1>framelogprob</span>,</td>
      </tr>
      <tr>
        <td id="L873" class="blob-num js-line-number" data-line-number="873"></td>
        <td id="LC873" class="blob-code blob-code-inner js-file-line">                                          <span class=pl-s1>post_comp</span>, <span class=pl-s1>fwdlattice</span>, <span class=pl-s1>bwdlattice</span>):</td>
      </tr>
      <tr>
        <td id="L874" class="blob-num js-line-number" data-line-number="874"></td>
        <td id="LC874" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L875" class="blob-num js-line-number" data-line-number="875"></td>
        <td id="LC875" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># TODO: support multiple frames</span></td>
      </tr>
      <tr>
        <td id="L876" class="blob-num js-line-number" data-line-number="876"></td>
        <td id="LC876" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L877" class="blob-num js-line-number" data-line-number="877"></td>
        <td id="LC877" class="blob-code blob-code-inner js-file-line">        <span class=pl-en>super</span>().<span class=pl-en>_accumulate_sufficient_statistics</span>(</td>
      </tr>
      <tr>
        <td id="L878" class="blob-num js-line-number" data-line-number="878"></td>
        <td id="LC878" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>stats</span>, <span class=pl-v>X</span>, <span class=pl-s1>framelogprob</span>, <span class=pl-s1>post_comp</span>, <span class=pl-s1>fwdlattice</span>, <span class=pl-s1>bwdlattice</span></td>
      </tr>
      <tr>
        <td id="L879" class="blob-num js-line-number" data-line-number="879"></td>
        <td id="LC879" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L880" class="blob-num js-line-number" data-line-number="880"></td>
        <td id="LC880" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L881" class="blob-num js-line-number" data-line-number="881"></td>
        <td id="LC881" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>n_samples</span>, <span class=pl-s1>_</span> <span class=pl-c1>=</span> <span class=pl-v>X</span>.<span class=pl-s1>shape</span></td>
      </tr>
      <tr>
        <td id="L882" class="blob-num js-line-number" data-line-number="882"></td>
        <td id="LC882" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L883" class="blob-num js-line-number" data-line-number="883"></td>
        <td id="LC883" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>stats</span>[<span class=pl-s>&#39;n_samples&#39;</span>] <span class=pl-c1>=</span> <span class=pl-s1>n_samples</span></td>
      </tr>
      <tr>
        <td id="L884" class="blob-num js-line-number" data-line-number="884"></td>
        <td id="LC884" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>stats</span>[<span class=pl-s>&#39;samples&#39;</span>] <span class=pl-c1>=</span> <span class=pl-v>X</span></td>
      </tr>
      <tr>
        <td id="L885" class="blob-num js-line-number" data-line-number="885"></td>
        <td id="LC885" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L886" class="blob-num js-line-number" data-line-number="886"></td>
        <td id="LC886" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>post_mix</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>zeros</span>((<span class=pl-s1>n_samples</span>, <span class=pl-s1>self</span>.<span class=pl-s1>n_components</span>, <span class=pl-s1>self</span>.<span class=pl-s1>n_mix</span>))</td>
      </tr>
      <tr>
        <td id="L887" class="blob-num js-line-number" data-line-number="887"></td>
        <td id="LC887" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>for</span> <span class=pl-s1>p</span> <span class=pl-c1>in</span> <span class=pl-en>range</span>(<span class=pl-s1>self</span>.<span class=pl-s1>n_components</span>):</td>
      </tr>
      <tr>
        <td id="L888" class="blob-num js-line-number" data-line-number="888"></td>
        <td id="LC888" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>log_denses</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-en>_compute_log_weighted_gaussian_densities</span>(<span class=pl-v>X</span>, <span class=pl-s1>p</span>)</td>
      </tr>
      <tr>
        <td id="L889" class="blob-num js-line-number" data-line-number="889"></td>
        <td id="LC889" class="blob-code blob-code-inner js-file-line">            <span class=pl-en>log_normalize</span>(<span class=pl-s1>log_denses</span>, <span class=pl-s1>axis</span><span class=pl-c1>=</span><span class=pl-c1>-</span><span class=pl-c1>1</span>)</td>
      </tr>
      <tr>
        <td id="L890" class="blob-num js-line-number" data-line-number="890"></td>
        <td id="LC890" class="blob-code blob-code-inner js-file-line">            <span class=pl-k>with</span> <span class=pl-s1>np</span>.<span class=pl-en>errstate</span>(<span class=pl-s1>under</span><span class=pl-c1>=</span><span class=pl-s>&quot;ignore&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L891" class="blob-num js-line-number" data-line-number="891"></td>
        <td id="LC891" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>post_mix</span>[:, <span class=pl-s1>p</span>, :] <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>exp</span>(<span class=pl-s1>log_denses</span>)</td>
      </tr>
      <tr>
        <td id="L892" class="blob-num js-line-number" data-line-number="892"></td>
        <td id="LC892" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L893" class="blob-num js-line-number" data-line-number="893"></td>
        <td id="LC893" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>with</span> <span class=pl-s1>np</span>.<span class=pl-en>errstate</span>(<span class=pl-s1>under</span><span class=pl-c1>=</span><span class=pl-s>&quot;ignore&quot;</span>):</td>
      </tr>
      <tr>
        <td id="L894" class="blob-num js-line-number" data-line-number="894"></td>
        <td id="LC894" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>post_comp_mix</span> <span class=pl-c1>=</span> <span class=pl-s1>post_comp</span>[:, :, <span class=pl-s1>np</span>.<span class=pl-s1>newaxis</span>] <span class=pl-c1>*</span> <span class=pl-s1>post_mix</span></td>
      </tr>
      <tr>
        <td id="L895" class="blob-num js-line-number" data-line-number="895"></td>
        <td id="LC895" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post_comp_mix&#39;</span>] <span class=pl-c1>=</span> <span class=pl-s1>post_comp_mix</span></td>
      </tr>
      <tr>
        <td id="L896" class="blob-num js-line-number" data-line-number="896"></td>
        <td id="LC896" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L897" class="blob-num js-line-number" data-line-number="897"></td>
        <td id="LC897" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post_mix_sum&#39;</span>] <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>sum</span>(<span class=pl-s1>post_comp_mix</span>, <span class=pl-s1>axis</span><span class=pl-c1>=</span><span class=pl-c1>0</span>)</td>
      </tr>
      <tr>
        <td id="L898" class="blob-num js-line-number" data-line-number="898"></td>
        <td id="LC898" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post_sum&#39;</span>] <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>sum</span>(<span class=pl-s1>post_comp</span>, <span class=pl-s1>axis</span><span class=pl-c1>=</span><span class=pl-c1>0</span>)</td>
      </tr>
      <tr>
        <td id="L899" class="blob-num js-line-number" data-line-number="899"></td>
        <td id="LC899" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L900" class="blob-num js-line-number" data-line-number="900"></td>
        <td id="LC900" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>stats</span>[<span class=pl-s>&#39;centered&#39;</span>] <span class=pl-c1>=</span> <span class=pl-v>X</span>[:, <span class=pl-s1>np</span>.<span class=pl-s1>newaxis</span>, <span class=pl-s1>np</span>.<span class=pl-s1>newaxis</span>, :] <span class=pl-c1>-</span> <span class=pl-s1>self</span>.<span class=pl-s1>means_</span></td>
      </tr>
      <tr>
        <td id="L901" class="blob-num js-line-number" data-line-number="901"></td>
        <td id="LC901" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L902" class="blob-num js-line-number" data-line-number="902"></td>
        <td id="LC902" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>_do_mstep</span>(<span class=pl-s1>self</span>, <span class=pl-s1>stats</span>):</td>
      </tr>
      <tr>
        <td id="L903" class="blob-num js-line-number" data-line-number="903"></td>
        <td id="LC903" class="blob-code blob-code-inner js-file-line">        <span class=pl-en>super</span>().<span class=pl-en>_do_mstep</span>(<span class=pl-s1>stats</span>)</td>
      </tr>
      <tr>
        <td id="L904" class="blob-num js-line-number" data-line-number="904"></td>
        <td id="LC904" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>nc</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_components</span></td>
      </tr>
      <tr>
        <td id="L905" class="blob-num js-line-number" data-line-number="905"></td>
        <td id="LC905" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>nf</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_features</span></td>
      </tr>
      <tr>
        <td id="L906" class="blob-num js-line-number" data-line-number="906"></td>
        <td id="LC906" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>nm</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>n_mix</span></td>
      </tr>
      <tr>
        <td id="L907" class="blob-num js-line-number" data-line-number="907"></td>
        <td id="LC907" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L908" class="blob-num js-line-number" data-line-number="908"></td>
        <td id="LC908" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>n_samples</span> <span class=pl-c1>=</span> <span class=pl-s1>stats</span>[<span class=pl-s>&#39;n_samples&#39;</span>]</td>
      </tr>
      <tr>
        <td id="L909" class="blob-num js-line-number" data-line-number="909"></td>
        <td id="LC909" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L910" class="blob-num js-line-number" data-line-number="910"></td>
        <td id="LC910" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Maximizing weights</span></td>
      </tr>
      <tr>
        <td id="L911" class="blob-num js-line-number" data-line-number="911"></td>
        <td id="LC911" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>alphas_minus_one</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>weights_prior</span> <span class=pl-c1>-</span> <span class=pl-c1>1</span></td>
      </tr>
      <tr>
        <td id="L912" class="blob-num js-line-number" data-line-number="912"></td>
        <td id="LC912" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>new_weights_numer</span> <span class=pl-c1>=</span> <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post_mix_sum&#39;</span>] <span class=pl-c1>+</span> <span class=pl-s1>alphas_minus_one</span></td>
      </tr>
      <tr>
        <td id="L913" class="blob-num js-line-number" data-line-number="913"></td>
        <td id="LC913" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>new_weights_denom</span> <span class=pl-c1>=</span> (</td>
      </tr>
      <tr>
        <td id="L914" class="blob-num js-line-number" data-line-number="914"></td>
        <td id="LC914" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post_sum&#39;</span>] <span class=pl-c1>+</span> <span class=pl-s1>np</span>.<span class=pl-en>sum</span>(<span class=pl-s1>alphas_minus_one</span>, <span class=pl-s1>axis</span><span class=pl-c1>=</span><span class=pl-c1>1</span>)</td>
      </tr>
      <tr>
        <td id="L915" class="blob-num js-line-number" data-line-number="915"></td>
        <td id="LC915" class="blob-code blob-code-inner js-file-line">        )[:, <span class=pl-s1>np</span>.<span class=pl-s1>newaxis</span>]</td>
      </tr>
      <tr>
        <td id="L916" class="blob-num js-line-number" data-line-number="916"></td>
        <td id="LC916" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>new_weights</span> <span class=pl-c1>=</span> <span class=pl-s1>new_weights_numer</span> <span class=pl-c1>/</span> <span class=pl-s1>new_weights_denom</span></td>
      </tr>
      <tr>
        <td id="L917" class="blob-num js-line-number" data-line-number="917"></td>
        <td id="LC917" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L918" class="blob-num js-line-number" data-line-number="918"></td>
        <td id="LC918" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Maximizing means</span></td>
      </tr>
      <tr>
        <td id="L919" class="blob-num js-line-number" data-line-number="919"></td>
        <td id="LC919" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>lambdas</span>, <span class=pl-s1>mus</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>means_weight</span>, <span class=pl-s1>self</span>.<span class=pl-s1>means_prior</span></td>
      </tr>
      <tr>
        <td id="L920" class="blob-num js-line-number" data-line-number="920"></td>
        <td id="LC920" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>new_means_numer</span> <span class=pl-c1>=</span> (</td>
      </tr>
      <tr>
        <td id="L921" class="blob-num js-line-number" data-line-number="921"></td>
        <td id="LC921" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>np</span>.<span class=pl-en>einsum</span>(<span class=pl-s>&#39;ijk,il-&gt;jkl&#39;</span>, <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post_comp_mix&#39;</span>], <span class=pl-s1>stats</span>[<span class=pl-s>&#39;samples&#39;</span>])</td>
      </tr>
      <tr>
        <td id="L922" class="blob-num js-line-number" data-line-number="922"></td>
        <td id="LC922" class="blob-code blob-code-inner js-file-line">            <span class=pl-c1>+</span> <span class=pl-s1>lambdas</span>[:, :, <span class=pl-s1>np</span>.<span class=pl-s1>newaxis</span>] <span class=pl-c1>*</span> <span class=pl-s1>mus</span></td>
      </tr>
      <tr>
        <td id="L923" class="blob-num js-line-number" data-line-number="923"></td>
        <td id="LC923" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L924" class="blob-num js-line-number" data-line-number="924"></td>
        <td id="LC924" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>new_means_denom</span> <span class=pl-c1>=</span> (<span class=pl-s1>stats</span>[<span class=pl-s>&#39;post_mix_sum&#39;</span>] <span class=pl-c1>+</span> <span class=pl-s1>lambdas</span>)[:, :, <span class=pl-s1>np</span>.<span class=pl-s1>newaxis</span>]</td>
      </tr>
      <tr>
        <td id="L925" class="blob-num js-line-number" data-line-number="925"></td>
        <td id="LC925" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>new_means</span> <span class=pl-c1>=</span> <span class=pl-s1>new_means_numer</span> <span class=pl-c1>/</span> <span class=pl-s1>new_means_denom</span></td>
      </tr>
      <tr>
        <td id="L926" class="blob-num js-line-number" data-line-number="926"></td>
        <td id="LC926" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L927" class="blob-num js-line-number" data-line-number="927"></td>
        <td id="LC927" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Maximizing covariances</span></td>
      </tr>
      <tr>
        <td id="L928" class="blob-num js-line-number" data-line-number="928"></td>
        <td id="LC928" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>centered_means</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>means_</span> <span class=pl-c1>-</span> <span class=pl-s1>mus</span></td>
      </tr>
      <tr>
        <td id="L929" class="blob-num js-line-number" data-line-number="929"></td>
        <td id="LC929" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L930" class="blob-num js-line-number" data-line-number="930"></td>
        <td id="LC930" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>if</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;full&#39;</span>:</td>
      </tr>
      <tr>
        <td id="L931" class="blob-num js-line-number" data-line-number="931"></td>
        <td id="LC931" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>centered</span> <span class=pl-c1>=</span> <span class=pl-s1>stats</span>[<span class=pl-s>&#39;centered&#39;</span>].<span class=pl-en>reshape</span>((<span class=pl-s1>n_samples</span>, <span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>, <span class=pl-s1>nf</span>, <span class=pl-c1>1</span>))</td>
      </tr>
      <tr>
        <td id="L932" class="blob-num js-line-number" data-line-number="932"></td>
        <td id="LC932" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>centered_t</span> <span class=pl-c1>=</span> <span class=pl-s1>stats</span>[<span class=pl-s>&#39;centered&#39;</span>].<span class=pl-en>reshape</span>((<span class=pl-s1>n_samples</span>, <span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>, <span class=pl-c1>1</span>, <span class=pl-s1>nf</span>))</td>
      </tr>
      <tr>
        <td id="L933" class="blob-num js-line-number" data-line-number="933"></td>
        <td id="LC933" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>centered_dots</span> <span class=pl-c1>=</span> <span class=pl-s1>centered</span> <span class=pl-c1>*</span> <span class=pl-s1>centered_t</span></td>
      </tr>
      <tr>
        <td id="L934" class="blob-num js-line-number" data-line-number="934"></td>
        <td id="LC934" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L935" class="blob-num js-line-number" data-line-number="935"></td>
        <td id="LC935" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>psis_t</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>transpose</span>(<span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span>, <span class=pl-s1>axes</span><span class=pl-c1>=</span>(<span class=pl-c1>0</span>, <span class=pl-c1>1</span>, <span class=pl-c1>3</span>, <span class=pl-c1>2</span>))</td>
      </tr>
      <tr>
        <td id="L936" class="blob-num js-line-number" data-line-number="936"></td>
        <td id="LC936" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>nus</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span></td>
      </tr>
      <tr>
        <td id="L937" class="blob-num js-line-number" data-line-number="937"></td>
        <td id="LC937" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L938" class="blob-num js-line-number" data-line-number="938"></td>
        <td id="LC938" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>centr_means_resh</span> <span class=pl-c1>=</span> <span class=pl-s1>centered_means</span>.<span class=pl-en>reshape</span>((<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>, <span class=pl-s1>nf</span>, <span class=pl-c1>1</span>))</td>
      </tr>
      <tr>
        <td id="L939" class="blob-num js-line-number" data-line-number="939"></td>
        <td id="LC939" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>centr_means_resh_t</span> <span class=pl-c1>=</span> <span class=pl-s1>centered_means</span>.<span class=pl-en>reshape</span>((<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>, <span class=pl-c1>1</span>, <span class=pl-s1>nf</span>))</td>
      </tr>
      <tr>
        <td id="L940" class="blob-num js-line-number" data-line-number="940"></td>
        <td id="LC940" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>centered_means_dots</span> <span class=pl-c1>=</span> <span class=pl-s1>centr_means_resh</span> <span class=pl-c1>*</span> <span class=pl-s1>centr_means_resh_t</span></td>
      </tr>
      <tr>
        <td id="L941" class="blob-num js-line-number" data-line-number="941"></td>
        <td id="LC941" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L942" class="blob-num js-line-number" data-line-number="942"></td>
        <td id="LC942" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>new_cov_numer</span> <span class=pl-c1>=</span> (</td>
      </tr>
      <tr>
        <td id="L943" class="blob-num js-line-number" data-line-number="943"></td>
        <td id="LC943" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>np</span>.<span class=pl-en>einsum</span>(</td>
      </tr>
      <tr>
        <td id="L944" class="blob-num js-line-number" data-line-number="944"></td>
        <td id="LC944" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s>&#39;ijk,ijklm-&gt;jklm&#39;</span>, <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post_comp_mix&#39;</span>], <span class=pl-s1>centered_dots</span>)</td>
      </tr>
      <tr>
        <td id="L945" class="blob-num js-line-number" data-line-number="945"></td>
        <td id="LC945" class="blob-code blob-code-inner js-file-line">                <span class=pl-c1>+</span> <span class=pl-s1>psis_t</span></td>
      </tr>
      <tr>
        <td id="L946" class="blob-num js-line-number" data-line-number="946"></td>
        <td id="LC946" class="blob-code blob-code-inner js-file-line">                <span class=pl-c1>+</span> <span class=pl-s1>lambdas</span>[:, :, <span class=pl-s1>np</span>.<span class=pl-s1>newaxis</span>, <span class=pl-s1>np</span>.<span class=pl-s1>newaxis</span>] <span class=pl-c1>*</span> <span class=pl-s1>centered_means_dots</span></td>
      </tr>
      <tr>
        <td id="L947" class="blob-num js-line-number" data-line-number="947"></td>
        <td id="LC947" class="blob-code blob-code-inner js-file-line">            )</td>
      </tr>
      <tr>
        <td id="L948" class="blob-num js-line-number" data-line-number="948"></td>
        <td id="LC948" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>new_cov_denom</span> <span class=pl-c1>=</span> (</td>
      </tr>
      <tr>
        <td id="L949" class="blob-num js-line-number" data-line-number="949"></td>
        <td id="LC949" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post_mix_sum&#39;</span>] <span class=pl-c1>+</span> <span class=pl-c1>1</span> <span class=pl-c1>+</span> <span class=pl-s1>nus</span> <span class=pl-c1>+</span> <span class=pl-s1>nf</span> <span class=pl-c1>+</span> <span class=pl-c1>1</span></td>
      </tr>
      <tr>
        <td id="L950" class="blob-num js-line-number" data-line-number="950"></td>
        <td id="LC950" class="blob-code blob-code-inner js-file-line">            )[:, :, <span class=pl-s1>np</span>.<span class=pl-s1>newaxis</span>, <span class=pl-s1>np</span>.<span class=pl-s1>newaxis</span>]</td>
      </tr>
      <tr>
        <td id="L951" class="blob-num js-line-number" data-line-number="951"></td>
        <td id="LC951" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>new_cov</span> <span class=pl-c1>=</span> <span class=pl-s1>new_cov_numer</span> <span class=pl-c1>/</span> <span class=pl-s1>new_cov_denom</span></td>
      </tr>
      <tr>
        <td id="L952" class="blob-num js-line-number" data-line-number="952"></td>
        <td id="LC952" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L953" class="blob-num js-line-number" data-line-number="953"></td>
        <td id="LC953" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>elif</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;diag&#39;</span>:</td>
      </tr>
      <tr>
        <td id="L954" class="blob-num js-line-number" data-line-number="954"></td>
        <td id="LC954" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>centered2</span> <span class=pl-c1>=</span> <span class=pl-s1>stats</span>[<span class=pl-s>&#39;centered&#39;</span>] <span class=pl-c1>**</span> <span class=pl-c1>2</span></td>
      </tr>
      <tr>
        <td id="L955" class="blob-num js-line-number" data-line-number="955"></td>
        <td id="LC955" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>centered_means2</span> <span class=pl-c1>=</span> <span class=pl-s1>centered_means</span> <span class=pl-c1>**</span> <span class=pl-c1>2</span></td>
      </tr>
      <tr>
        <td id="L956" class="blob-num js-line-number" data-line-number="956"></td>
        <td id="LC956" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L957" class="blob-num js-line-number" data-line-number="957"></td>
        <td id="LC957" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>alphas</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span></td>
      </tr>
      <tr>
        <td id="L958" class="blob-num js-line-number" data-line-number="958"></td>
        <td id="LC958" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>betas</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span></td>
      </tr>
      <tr>
        <td id="L959" class="blob-num js-line-number" data-line-number="959"></td>
        <td id="LC959" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L960" class="blob-num js-line-number" data-line-number="960"></td>
        <td id="LC960" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>new_cov_numer</span> <span class=pl-c1>=</span> (</td>
      </tr>
      <tr>
        <td id="L961" class="blob-num js-line-number" data-line-number="961"></td>
        <td id="LC961" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>np</span>.<span class=pl-en>einsum</span>(<span class=pl-s>&#39;ijk,ijkl-&gt;jkl&#39;</span>, <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post_comp_mix&#39;</span>], <span class=pl-s1>centered2</span>)</td>
      </tr>
      <tr>
        <td id="L962" class="blob-num js-line-number" data-line-number="962"></td>
        <td id="LC962" class="blob-code blob-code-inner js-file-line">                <span class=pl-c1>+</span> <span class=pl-s1>lambdas</span>[:, :, <span class=pl-s1>np</span>.<span class=pl-s1>newaxis</span>] <span class=pl-c1>*</span> <span class=pl-s1>centered_means2</span></td>
      </tr>
      <tr>
        <td id="L963" class="blob-num js-line-number" data-line-number="963"></td>
        <td id="LC963" class="blob-code blob-code-inner js-file-line">                <span class=pl-c1>+</span> <span class=pl-c1>2</span> <span class=pl-c1>*</span> <span class=pl-s1>betas</span></td>
      </tr>
      <tr>
        <td id="L964" class="blob-num js-line-number" data-line-number="964"></td>
        <td id="LC964" class="blob-code blob-code-inner js-file-line">            )</td>
      </tr>
      <tr>
        <td id="L965" class="blob-num js-line-number" data-line-number="965"></td>
        <td id="LC965" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>new_cov_denom</span> <span class=pl-c1>=</span> (</td>
      </tr>
      <tr>
        <td id="L966" class="blob-num js-line-number" data-line-number="966"></td>
        <td id="LC966" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post_mix_sum&#39;</span>][:, :, <span class=pl-s1>np</span>.<span class=pl-s1>newaxis</span>] <span class=pl-c1>+</span> <span class=pl-c1>1</span> <span class=pl-c1>+</span> <span class=pl-c1>2</span> <span class=pl-c1>*</span> (<span class=pl-s1>alphas</span> <span class=pl-c1>+</span> <span class=pl-c1>1</span>)</td>
      </tr>
      <tr>
        <td id="L967" class="blob-num js-line-number" data-line-number="967"></td>
        <td id="LC967" class="blob-code blob-code-inner js-file-line">            )</td>
      </tr>
      <tr>
        <td id="L968" class="blob-num js-line-number" data-line-number="968"></td>
        <td id="LC968" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>new_cov</span> <span class=pl-c1>=</span> <span class=pl-s1>new_cov_numer</span> <span class=pl-c1>/</span> <span class=pl-s1>new_cov_denom</span></td>
      </tr>
      <tr>
        <td id="L969" class="blob-num js-line-number" data-line-number="969"></td>
        <td id="LC969" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L970" class="blob-num js-line-number" data-line-number="970"></td>
        <td id="LC970" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>elif</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;spherical&#39;</span>:</td>
      </tr>
      <tr>
        <td id="L971" class="blob-num js-line-number" data-line-number="971"></td>
        <td id="LC971" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>centered_norm2</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>sum</span>(<span class=pl-s1>stats</span>[<span class=pl-s>&#39;centered&#39;</span>] <span class=pl-c1>**</span> <span class=pl-c1>2</span>, <span class=pl-s1>axis</span><span class=pl-c1>=</span><span class=pl-c1>-</span><span class=pl-c1>1</span>)</td>
      </tr>
      <tr>
        <td id="L972" class="blob-num js-line-number" data-line-number="972"></td>
        <td id="LC972" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L973" class="blob-num js-line-number" data-line-number="973"></td>
        <td id="LC973" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>alphas</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span></td>
      </tr>
      <tr>
        <td id="L974" class="blob-num js-line-number" data-line-number="974"></td>
        <td id="LC974" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>betas</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span></td>
      </tr>
      <tr>
        <td id="L975" class="blob-num js-line-number" data-line-number="975"></td>
        <td id="LC975" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L976" class="blob-num js-line-number" data-line-number="976"></td>
        <td id="LC976" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>centered_means_norm2</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>sum</span>(<span class=pl-s1>centered_means</span> <span class=pl-c1>**</span> <span class=pl-c1>2</span>, <span class=pl-s1>axis</span><span class=pl-c1>=</span><span class=pl-c1>-</span><span class=pl-c1>1</span>)</td>
      </tr>
      <tr>
        <td id="L977" class="blob-num js-line-number" data-line-number="977"></td>
        <td id="LC977" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L978" class="blob-num js-line-number" data-line-number="978"></td>
        <td id="LC978" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>new_cov_numer</span> <span class=pl-c1>=</span> (</td>
      </tr>
      <tr>
        <td id="L979" class="blob-num js-line-number" data-line-number="979"></td>
        <td id="LC979" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>np</span>.<span class=pl-en>einsum</span>(</td>
      </tr>
      <tr>
        <td id="L980" class="blob-num js-line-number" data-line-number="980"></td>
        <td id="LC980" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s>&#39;ijk,ijk-&gt;jk&#39;</span>, <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post_comp_mix&#39;</span>], <span class=pl-s1>centered_norm2</span>)</td>
      </tr>
      <tr>
        <td id="L981" class="blob-num js-line-number" data-line-number="981"></td>
        <td id="LC981" class="blob-code blob-code-inner js-file-line">                <span class=pl-c1>+</span> <span class=pl-s1>lambdas</span> <span class=pl-c1>*</span> <span class=pl-s1>centered_means_norm2</span></td>
      </tr>
      <tr>
        <td id="L982" class="blob-num js-line-number" data-line-number="982"></td>
        <td id="LC982" class="blob-code blob-code-inner js-file-line">                <span class=pl-c1>+</span> <span class=pl-c1>2</span> <span class=pl-c1>*</span> <span class=pl-s1>betas</span></td>
      </tr>
      <tr>
        <td id="L983" class="blob-num js-line-number" data-line-number="983"></td>
        <td id="LC983" class="blob-code blob-code-inner js-file-line">            )</td>
      </tr>
      <tr>
        <td id="L984" class="blob-num js-line-number" data-line-number="984"></td>
        <td id="LC984" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>new_cov_denom</span> <span class=pl-c1>=</span> <span class=pl-s1>nf</span> <span class=pl-c1>*</span> (<span class=pl-s1>stats</span>[<span class=pl-s>&#39;post_mix_sum&#39;</span>] <span class=pl-c1>+</span> <span class=pl-c1>1</span>) <span class=pl-c1>+</span> <span class=pl-c1>2</span> <span class=pl-c1>*</span> (<span class=pl-s1>alphas</span> <span class=pl-c1>+</span> <span class=pl-c1>1</span>)</td>
      </tr>
      <tr>
        <td id="L985" class="blob-num js-line-number" data-line-number="985"></td>
        <td id="LC985" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>new_cov</span> <span class=pl-c1>=</span> <span class=pl-s1>new_cov_numer</span> <span class=pl-c1>/</span> <span class=pl-s1>new_cov_denom</span></td>
      </tr>
      <tr>
        <td id="L986" class="blob-num js-line-number" data-line-number="986"></td>
        <td id="LC986" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L987" class="blob-num js-line-number" data-line-number="987"></td>
        <td id="LC987" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>elif</span> <span class=pl-s1>self</span>.<span class=pl-s1>covariance_type</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;tied&#39;</span>:</td>
      </tr>
      <tr>
        <td id="L988" class="blob-num js-line-number" data-line-number="988"></td>
        <td id="LC988" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>centered</span> <span class=pl-c1>=</span> <span class=pl-s1>stats</span>[<span class=pl-s>&#39;centered&#39;</span>].<span class=pl-en>reshape</span>((<span class=pl-s1>n_samples</span>, <span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>, <span class=pl-s1>nf</span>, <span class=pl-c1>1</span>))</td>
      </tr>
      <tr>
        <td id="L989" class="blob-num js-line-number" data-line-number="989"></td>
        <td id="LC989" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>centered_t</span> <span class=pl-c1>=</span> <span class=pl-s1>stats</span>[<span class=pl-s>&#39;centered&#39;</span>].<span class=pl-en>reshape</span>((<span class=pl-s1>n_samples</span>, <span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>, <span class=pl-c1>1</span>, <span class=pl-s1>nf</span>))</td>
      </tr>
      <tr>
        <td id="L990" class="blob-num js-line-number" data-line-number="990"></td>
        <td id="LC990" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>centered_dots</span> <span class=pl-c1>=</span> <span class=pl-s1>centered</span> <span class=pl-c1>*</span> <span class=pl-s1>centered_t</span></td>
      </tr>
      <tr>
        <td id="L991" class="blob-num js-line-number" data-line-number="991"></td>
        <td id="LC991" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L992" class="blob-num js-line-number" data-line-number="992"></td>
        <td id="LC992" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>psis_t</span> <span class=pl-c1>=</span> <span class=pl-s1>np</span>.<span class=pl-en>transpose</span>(<span class=pl-s1>self</span>.<span class=pl-s1>covars_prior</span>, <span class=pl-s1>axes</span><span class=pl-c1>=</span>(<span class=pl-c1>0</span>, <span class=pl-c1>2</span>, <span class=pl-c1>1</span>))</td>
      </tr>
      <tr>
        <td id="L993" class="blob-num js-line-number" data-line-number="993"></td>
        <td id="LC993" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>nus</span> <span class=pl-c1>=</span> <span class=pl-s1>self</span>.<span class=pl-s1>covars_weight</span></td>
      </tr>
      <tr>
        <td id="L994" class="blob-num js-line-number" data-line-number="994"></td>
        <td id="LC994" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L995" class="blob-num js-line-number" data-line-number="995"></td>
        <td id="LC995" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>centr_means_resh</span> <span class=pl-c1>=</span> <span class=pl-s1>centered_means</span>.<span class=pl-en>reshape</span>((<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>, <span class=pl-s1>nf</span>, <span class=pl-c1>1</span>))</td>
      </tr>
      <tr>
        <td id="L996" class="blob-num js-line-number" data-line-number="996"></td>
        <td id="LC996" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>centr_means_resh_t</span> <span class=pl-c1>=</span> <span class=pl-s1>centered_means</span>.<span class=pl-en>reshape</span>((<span class=pl-s1>nc</span>, <span class=pl-s1>nm</span>, <span class=pl-c1>1</span>, <span class=pl-s1>nf</span>))</td>
      </tr>
      <tr>
        <td id="L997" class="blob-num js-line-number" data-line-number="997"></td>
        <td id="LC997" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>centered_means_dots</span> <span class=pl-c1>=</span> <span class=pl-s1>centr_means_resh</span> <span class=pl-c1>*</span> <span class=pl-s1>centr_means_resh_t</span></td>
      </tr>
      <tr>
        <td id="L998" class="blob-num js-line-number" data-line-number="998"></td>
        <td id="LC998" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L999" class="blob-num js-line-number" data-line-number="999"></td>
        <td id="LC999" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>lambdas_cmdots_prod_sum</span> <span class=pl-c1>=</span> (</td>
      </tr>
      <tr>
        <td id="L1000" class="blob-num js-line-number" data-line-number="1000"></td>
        <td id="LC1000" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>np</span>.<span class=pl-en>einsum</span>(<span class=pl-s>&#39;ij,ijkl-&gt;ikl&#39;</span>, <span class=pl-s1>lambdas</span>, <span class=pl-s1>centered_means_dots</span>))</td>
      </tr>
      <tr>
        <td id="L1001" class="blob-num js-line-number" data-line-number="1001"></td>
        <td id="LC1001" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1002" class="blob-num js-line-number" data-line-number="1002"></td>
        <td id="LC1002" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>new_cov_numer</span> <span class=pl-c1>=</span> (</td>
      </tr>
      <tr>
        <td id="L1003" class="blob-num js-line-number" data-line-number="1003"></td>
        <td id="LC1003" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>np</span>.<span class=pl-en>einsum</span>(</td>
      </tr>
      <tr>
        <td id="L1004" class="blob-num js-line-number" data-line-number="1004"></td>
        <td id="LC1004" class="blob-code blob-code-inner js-file-line">                    <span class=pl-s>&#39;ijk,ijklm-&gt;jlm&#39;</span>, <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post_comp_mix&#39;</span>], <span class=pl-s1>centered_dots</span>)</td>
      </tr>
      <tr>
        <td id="L1005" class="blob-num js-line-number" data-line-number="1005"></td>
        <td id="LC1005" class="blob-code blob-code-inner js-file-line">                <span class=pl-c1>+</span> <span class=pl-s1>lambdas_cmdots_prod_sum</span> <span class=pl-c1>+</span> <span class=pl-s1>psis_t</span>)</td>
      </tr>
      <tr>
        <td id="L1006" class="blob-num js-line-number" data-line-number="1006"></td>
        <td id="LC1006" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>new_cov_denom</span> <span class=pl-c1>=</span> (</td>
      </tr>
      <tr>
        <td id="L1007" class="blob-num js-line-number" data-line-number="1007"></td>
        <td id="LC1007" class="blob-code blob-code-inner js-file-line">                <span class=pl-s1>stats</span>[<span class=pl-s>&#39;post_sum&#39;</span>] <span class=pl-c1>+</span> <span class=pl-s1>nm</span> <span class=pl-c1>+</span> <span class=pl-s1>nus</span> <span class=pl-c1>+</span> <span class=pl-s1>nf</span> <span class=pl-c1>+</span> <span class=pl-c1>1</span></td>
      </tr>
      <tr>
        <td id="L1008" class="blob-num js-line-number" data-line-number="1008"></td>
        <td id="LC1008" class="blob-code blob-code-inner js-file-line">            )[:, <span class=pl-s1>np</span>.<span class=pl-s1>newaxis</span>, <span class=pl-s1>np</span>.<span class=pl-s1>newaxis</span>]</td>
      </tr>
      <tr>
        <td id="L1009" class="blob-num js-line-number" data-line-number="1009"></td>
        <td id="LC1009" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>new_cov</span> <span class=pl-c1>=</span> <span class=pl-s1>new_cov_numer</span> <span class=pl-c1>/</span> <span class=pl-s1>new_cov_denom</span></td>
      </tr>
      <tr>
        <td id="L1010" class="blob-num js-line-number" data-line-number="1010"></td>
        <td id="LC1010" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1011" class="blob-num js-line-number" data-line-number="1011"></td>
        <td id="LC1011" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># Assigning new values to class members</span></td>
      </tr>
      <tr>
        <td id="L1012" class="blob-num js-line-number" data-line-number="1012"></td>
        <td id="LC1012" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>weights_</span> <span class=pl-c1>=</span> <span class=pl-s1>new_weights</span></td>
      </tr>
      <tr>
        <td id="L1013" class="blob-num js-line-number" data-line-number="1013"></td>
        <td id="LC1013" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>means_</span> <span class=pl-c1>=</span> <span class=pl-s1>new_means</span></td>
      </tr>
      <tr>
        <td id="L1014" class="blob-num js-line-number" data-line-number="1014"></td>
        <td id="LC1014" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>self</span>.<span class=pl-s1>covars_</span> <span class=pl-c1>=</span> <span class=pl-s1>new_cov</span></td>
      </tr>
</table>

  <details class="details-reset details-overlay BlobToolbar position-absolute js-file-line-actions dropdown d-none" aria-hidden="true">
    <summary class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1" aria-label="Inline file action toolbar">
      <svg class="octicon octicon-kebab-horizontal" viewBox="0 0 13 16" version="1.1" width="13" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z"/></svg>
    </summary>
    <details-menu>
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2" style="width:185px">
        <li>
          <clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-lines" style="cursor:pointer;">
            Copy lines
          </clipboard-copy>
        </li>
        <li>
          <clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-permalink" style="cursor:pointer;">
            Copy permalink
          </clipboard-copy>
        </li>
        <li><a class="dropdown-item js-update-url-with-hash" id="js-view-git-blame" role="menuitem" href="/hmmlearn/hmmlearn/blame/0e9274cb138427919c13ef79f11a7358c4e2b4a9/lib/hmmlearn/hmm.py">View git blame</a></li>
          <li><a class="dropdown-item" id="js-new-issue" role="menuitem" href="/hmmlearn/hmmlearn/issues/new">Reference in new issue</a></li>
      </ul>
    </details-menu>
  </details>

  </div>

    </div>

  

  <details class="details-reset details-overlay details-overlay-dark">
    <summary data-hotkey="l" aria-label="Jump to line"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form Box-body d-flex" action="" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
        <button type="submit" class="btn" data-close-dialog>Go</button>
</form>    </details-dialog>
  </details>

    <div class="Popover anim-scale-in js-tagsearch-popover"
     hidden
     data-tagsearch-url="/hmmlearn/hmmlearn/find-symbols"
     data-tagsearch-ref="master"
     data-tagsearch-path="lib/hmmlearn/hmm.py"
     data-tagsearch-lang="Python"
     data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.click_on_symbol&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;click_on_symbol&quot;,&quot;repository_id&quot;:18031064,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/hmmlearn/hmmlearn/blob/master/lib/hmmlearn/hmm.py&quot;,&quot;user_id&quot;:58004482}}"
     data-hydro-click-hmac="f48eb3bd98c60fef975db9970c40b276e624f2ffbf0b7cd9cb26e5040c8f5254">
  <div class="Popover-message Popover-message--large Popover-message--top-left TagsearchPopover mt-1 mb-4 mx-auto Box box-shadow-large">
    <div class="TagsearchPopover-content js-tagsearch-popover-content overflow-auto" style="will-change:transform;">
    </div>
  </div>
</div>



  </div>
</div>

    </main>
  </div>
  

  </div>

        
<div class="footer container-lg width-full p-responsive" role="contentinfo">
  <div class="position-relative d-flex flex-row-reverse flex-lg-row flex-wrap flex-lg-nowrap flex-justify-center flex-lg-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
      <li class="mr-3 mr-lg-0">&copy; 2020 GitHub, Inc.</li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://githubstatus.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon d-none d-lg-block mx-lg-4" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 000 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 00.01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    <script crossorigin="anonymous" async="async" integrity="sha512-VTkKwyyXYz1e8w0v/7LXDKSa7yMy1qEQofgf/5bGrUv8wpbpaZxx5S3Uc6oYrvbOe432HJdJG5qsFdM9sbP+wg==" type="application/javascript" id="js-conditional-compat" data-src="https://github.githubassets.com/assets/compat-bootstrap-55390ac3.js"></script>
    <script crossorigin="anonymous" async="async" integrity="sha512-3yNijdFdVDBZQDWrBvMeD2J9gyXwI5MKUMJSWdEGP44DgS4NEPQw2TmVlDdNAWrseJO5C/sXBSTrL24DvGMDJw==" type="application/javascript" src="https://github.githubassets.com/assets/vendor-df23628d.js"></script>
    <script crossorigin="anonymous" integrity="sha512-WZp98krTVri8yp2f8bpVGoTndKcChquCeXJdlvMy65oKppZPzZ52UwQQl0tO7kHoFC75L7MlBMxY3NhWju6CRg==" type="application/javascript" src="https://github.githubassets.com/assets/frameworks-599a7df2.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-Lap1+NRBH7wIWfmCDnMs6d5Keym1I0bJd3QDvtvFy+lfSMcvPzPioITh++pTkwx/3BvvsDvTYjSlQ6pptb8cGQ==" type="application/javascript" src="https://github.githubassets.com/assets/github-bootstrap-2daa75f8.js"></script>
    
    
    
  <div class="js-stale-session-flash flash flash-warn flash-banner" hidden
    >
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 000 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 00.01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <span class="js-stale-session-flash-signed-in" hidden>You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="js-stale-session-flash-signed-out" hidden>You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

  <div aria-live="polite" class="js-global-screen-reader-notice sr-only"></div>

  </body>
</html>

