const KEY='lolos-scrap-collect-demo-v1';
export function loadState(){try{return JSON.parse(localStorage.getItem(KEY)||'{}')}catch{return {}}}
export function saveState(state){try{localStorage.setItem(KEY,JSON.stringify(state))}catch{/* browser storage unavailable; session still works */}}
