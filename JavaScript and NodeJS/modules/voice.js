var ResponsiveVoice = function(){
var self = this;
var responsivevoices = [
{name: 'UK English Female', voiceIDs: [3,5,1,6,7,8] },
{name: 'UK English Male', voiceIDs: [0,4,2,6,7,8] },
{name: 'US English Female',voiceIDs: [39,40,41,42,43,44] },
{name: 'Spanish Female',voiceIDs: [19,16,17,18,20,15] },
{name: 'French Female',voiceIDs: [21,22,23,26] },
{name: 'Deutsch Female',voiceIDs: [27,28,29,30,31,32] },
{name: 'Italian Female',voiceIDs: [33,34,35,36,37,38] },
{name: 'Hungarian Female',voiceIDs: [9,10,11] },
{name: 'Serbian Male',voiceIDs: [12] },
{name: 'Croatian Male',voiceIDs: [13] },
{name: 'Bosnian Male',voiceIDs: [14] },
{name: 'Fallback UK Female', voiceIDs: [8] }
];
var voicecollection = [
{name: 'Google UK English Male'},{name: 'Agnes'},{name: 'Daniel Compact'},{name: 'Google UK English Female'},{name: 'en-GB', rate: 0.5, pitch: 1}, {name: 'en-AU', rate: 0.5, pitch: 1},{name: 'inglés Reino Unido'},{name: 'English United Kingdom'},{name: 'Fallback en-GB Female', lang: 'en-GB', fallbackvoice: true},{name: 'Eszter Compact'},{name: 'hu-HU', rate: 0.4},{name: 'Fallback Hungarian', lang: 'hu', fallbackvoice:true},{name: 'Fallback Serbian', lang: 'sr', fallbackvoice:true},{name: 'Fallback Croatian',lang: 'hr', fallbackvoice:true},{name: 'Fallback Bosnian',lang: 'bs', fallbackvoice:true},
{name: 'Fallback Spanish',lang: 'es', fallbackvoice:true},{name: 'Spanish Spain'},{name: 'español España'},{name: 'Diego Compact', rate: 0.3},{name: 'Google Español'},{name: 'es-ES', rate: 0.3},
{name: 'Google Français'},{name: 'French France'},{name: 'francés Francia'},{name: 'Virginie Compact', rate: 0.5},{name: 'fr-FR', rate: 0.5},{name: 'Fallback French',lang: 'fr', fallbackvoice:true},
{name: 'Google Deutsch'},{name: 'German Germany'},{name: 'alemán Alemania'},{name: 'Yannick Compact', rate: 0.5},{name: 'de-DE', rate: 0.5},{name: 'Fallback Deutsch',lang: 'de', fallbackvoice:true},
{name: 'Google Italiano'},{name: 'Italian Italy'},{name: 'italiano Italia'},{name: 'Paolo Compact', rate: 0.5},{name: 'it-IT', rate: 0.5},{name: 'Fallback Italian',lang: 'it', fallbackvoice:true},
{name: 'Google US English'},{name: 'English United States'},{name: 'inglés Estados Unidos'},{name: 'Vicki'},{name: 'en-US', rate: 0.5},{name: 'Fallback English',lang: 'en-US', fallbackvoice:true},
];
var systemvoices;
var CHARACTER_LIMIT = 100;
var VOICESUPPORT_ATTEMPTLIMIT = 5;
var voicesupport_attempts = 0;
var fallbackMode = false;
this.fallback_playing = false;
this.fallback_parts = null;
this.fallback_part_index = 0;
this.fallback_audio = null;
if (typeof speechSynthesis != 'undefined') {
speechSynthesis.onvoiceschanged = function() {
systemvoices = window.speechSynthesis.getVoices();
if (self.OnVoiceReady!=null) {
self.OnVoiceReady.call();
}
};
}
this.default_rv = responsivevoices[0];
this.OnVoiceReady = null;
if (typeof $ === 'undefined') {
document.addEventListener('DOMContentLoaded',function(){
init();
});
}else{
$(document).ready(function() {
init();
});
}
function init() {
if (typeof speechSynthesis === 'undefined') {
enableFallbackMode();
} else {
setTimeout(function(){
var gsvinterval = setInterval(function() {
var v = window.speechSynthesis.getVoices();
if (v.length==0 && (systemvoices==null || systemvoices.length==0)) {
console.log('Voice support NOT ready');
voicesupport_attempts++;
if (voicesupport_attempts > VOICESUPPORT_ATTEMPTLIMIT) {
clearInterval(gsvinterval);
enableFallbackMode();
}
}else{
console.log('Voice support ready');
clearInterval(gsvinterval);
systemvoices = v;
mapRVs();
if (self.OnVoiceReady!=null)
self.OnVoiceReady.call();
}
},100);
},100);
}
}
function enableFallbackMode() {
fallbackMode = true;
console.log('Voice not supported. Using fallback mode');
mapRVs();
if (self.OnVoiceReady!=null)
self.OnVoiceReady.call();
}
this.getVoices = function() {
var v = [];
for (var i=0; i<responsivevoices.length; i++) {
v.push( { name: responsivevoices[i].name });
}
return v;
}
this.speak = function(text, voicename) {
var multipartText = [];
if (text.length>CHARACTER_LIMIT) {
var tmptxt = text;
while(tmptxt.length>CHARACTER_LIMIT) {
var p = tmptxt.search(/[:!?.;]+/);
var part = '';
if (p==-1 || p>=CHARACTER_LIMIT ) {
p = tmptxt.search(/[,]+/);
}
if (p==-1 || p>=CHARACTER_LIMIT) {
var words = tmptxt.split(' ');
for (var i=0; i<words.length; i++) {
if (part.length + words[i].length +1 >CHARACTER_LIMIT)
break;
part += (i!=0?' ':'') + words[i];
}
} else {
part = tmptxt.substr(0, p+1);
}
tmptxt = tmptxt.substr(part.length, tmptxt.length-part.length);
multipartText.push(part);
}
if (tmptxt.length>0) {
multipartText.push(tmptxt);
}
}else{
multipartText.push(text);
}
var rv;
if (voicename==null) {
rv = self.default_rv;
}else{
rv = getResponsiveVoice(voicename);
}
var profile = {};
if (rv.mappedProfile!=null) {
profile = rv.mappedProfile;
}else{
profile.systemvoice = getMatchedVoice(rv);
profile.collectionvoice = {};
if (profile.systemvoice==null) {
console.log('ERROR: No voice found for: ' + voicename);
return;
}
}
if (profile.collectionvoice.fallbackvoice==true) {
fallbackMode = true;
self.fallback_parts = [];
}else{
fallbackMode = false;
}
for (var i=0; i<multipartText.length; i++) {
if (!fallbackMode) {
var msg = new SpeechSynthesisUtterance();
msg.voice = profile.systemvoice;
msg.voiceURI = profile.systemvoice.voiceURI;
msg.volume = profile.collectionvoice.volume || profile.systemvoice.volume || 1;msg.rate = profile.collectionvoice.rate || profile.systemvoice.rate || 1;msg.pitch = profile.collectionvoice.pitch || profile.systemvoice.pitch || 1;msg.text = multipartText[i];
msg.lang = profile.collectionvoice.lang || profile.systemvoice.lang;
msg.onend = self.OnFinishedPlaying;
msg.onerror = function(e){
console.log('Error');
console.log(e);
};
speechSynthesis.speak(msg);
}else{
var url = 'http://www.corsproxy.com/translate.google.com/translate_tts?ie=UTF-8&q=' + multipartText[i] + '&tl=' + profile.collectionvoice.lang || profile.systemvoice.lang || 'en-US';
var audio = new Audio(url);
audio.playbackRate = 1;
audio.preload = 'auto';
audio.volume = profile.collectionvoice.volume || profile.systemvoice.volume || 1;self.fallback_parts.push(audio);
}
}
if (fallbackMode)
self.fallback_startPlaying();
}
this.fallback_startPlaying = function() {
self.fallback_part_index = 0;
self.fallback_finishedplaying();
}
this.fallback_finishedplaying = function(e) {
self.fallback_audio = self.fallback_parts[self.fallback_part_index];
self.fallback_audio.play();
self.fallback_part_index ++;
if (self.fallback_part_index < self.fallback_parts.length) {
self.fallback_audio.addEventListener('ended', self.fallback_finishedplaying);
}
}
this.cancel = function() {
if (fallbackMode)
self.fallback_audio.pause();
else
speechSynthesis.cancel();
}
this.voiceSupport = function() {
return ('speechSynthesis' in window);
}
this.OnFinishedPlaying = function(event) {
}
this.setDefaultVoice = function(voicename) {
var vr = getResponsiveVoice(voicename);
if (vr!=null) {
self.default_vr = vr;
}
}
function mapRVs() {
for (var i=0; i<responsivevoices.length; i++) {
var rv = responsivevoices[i];
for (var j=0; j<rv.voiceIDs.length; j++) {
var vcoll = voicecollection[rv.voiceIDs[j]];
if (vcoll.fallbackvoice != true) {
var v = getSystemVoice(vcoll.name);
if (v!=null) {
rv.mappedProfile = {
systemvoice: v,
collectionvoice: vcoll
};
console.log("Mapped " + rv.name + " to " + v.name);
break;
}
}else {
rv.mappedProfile = {
systemvoice: {},
collectionvoice: vcoll
};
console.log("Mapped " + rv.name + " to " + vcoll.lang + " fallback voice");
break;
}
}
}
}
function getMatchedVoice(rv) {
for (var i=0; i<rv.voiceIDs.length; i++) {
var v = getSystemVoice(voicecollection[rv.voiceIDs[i]].name);
if (v!=null)
return v;
}
return null;
}
function getSystemVoice(name) {
if (typeof systemvoices === 'undefined') return null;
for (var i=0; i<systemvoices.length; i++) {
if (systemvoices[i].name == name)
return systemvoices[i];
}
return null;
}
function getResponsiveVoice(name) {
for (var i=0; i<responsivevoices.length; i++) {
if (responsivevoices[i].name == name) {
return responsivevoices[i];
}
}
return null;
}
}
var responsiveVoice = new ResponsiveVoice();
