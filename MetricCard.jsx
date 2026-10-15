import { ArrowUpRight } from 'lucide-react';
export function MetricCard({ title, value, change, icon: Icon, tone = 'green' }) {
 return <article className="metric-card"><div className="metric-top"><span className="metric-title">{title}</span><span className={`metric-icon ${tone}`}><Icon size={18}/></span></div><div className="metric-value">{value}</div><div className="metric-foot"><span className="positive"><ArrowUpRight size={13}/></span>{change}</div></article>;
}
