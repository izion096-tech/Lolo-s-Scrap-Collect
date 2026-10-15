export function validateIntake(form){
 const blockers=[],warnings=[];
 if(!form.sellerRef)blockers.push('Select an internal supplier reference.');
 if(!form.material?.code)blockers.push('Select a material grade.');
 if(!Number.isFinite(form.netKg)||form.netKg<=0)blockers.push('Net weight must be greater than zero.');
 if(!form.counterpartyVerified)blockers.push('Counterparty verification is pending.');
 if(!form.sourceRecorded)blockers.push('Record source/provenance before saving.');
 if(['Cash','Pending'].includes(form.paymentMethod))blockers.push('Select an approved electronic payment method for this demo.');
 if(form.provenance!=='Documented')warnings.push('Material provenance needs authorised human review.');
 if(form.hazard)warnings.push('Hazard/suspicious-load flag set. Isolate and escalate under site procedure.');
 if(form.material?.code==='CAB-BURNT')warnings.push('Burnt cable requires an explanation and compliance review.');
 if(form.material?.hazardLevel==='high')warnings.push('Specialist handling class: confirm safe acceptance and storage.');
 return {blockers,warnings};
}
export function getReviewFlags(intakes){return intakes.flatMap(x=>{const reasons=[];if(x.status==='Review')reasons.push('Load is held for authorised review.');if(x.provenance==='Unknown'||x.provenance==='Disputed')reasons.push('Provenance needs confirmation.');if(x.hazard)reasons.push('Hazard/suspicious-load flag is set.');if(x.materialCode==='CAB-BURNT')reasons.push('Burnt cable requires compliance review.');if(x.netKg>500)reasons.push('Large load: confirm scale record and source.');if(x.estimatedValue>25000)reasons.push('High transaction value: apply the approved authorisation threshold.');return reasons.length?[{id:x.id,title:`Review ${x.id}`,reason:reasons.join(' ')}]:[]})}
