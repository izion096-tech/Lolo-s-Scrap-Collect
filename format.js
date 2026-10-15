export const formatCurrency = (value) => new Intl.NumberFormat('en-ZA',{style:'currency',currency:'ZAR',maximumFractionDigits:2}).format(Number(value||0));
export const formatKg = (value) => `${new Intl.NumberFormat('en-ZA',{maximumFractionDigits:1}).format(Number(value||0))} kg`;
