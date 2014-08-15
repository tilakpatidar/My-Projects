function varargout = issue(varargin)
% ISSUE M-file for issue.fig
%      ISSUE, by itself, creates a new ISSUE or raises the existing
%      singleton*.
%
%      H = ISSUE returns the handle to a new ISSUE or the handle to
%      the existing singleton*.
%
%      ISSUE('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in ISSUE.M with the given input arguments.
%
%      ISSUE('Property','Value',...) creates a new ISSUE or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before issue_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to issue_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help issue

% Last Modified by GUIDE v2.5 26-Oct-2013 19:59:56

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @issue_OpeningFcn, ...
                   'gui_OutputFcn',  @issue_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before issue is made visible.
function issue_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to issue (see VARARGIN)

% Choose default command line output for issue
handles.output = hObject;
handles.initial_parameter=varargin{1};
sqlpass=handles.initial_parameter;
% Update handles structure
guidata(hObject, handles);

% UIWAIT makes issue wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = issue_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
tdate=date;
tdate=datestr(tdate,31);
set(handles.edit3,'String',tdate);
% Get default command line output from handles structure
varargout{1} = handles.output;
imshow('issue.jpg',handles.axes1);
function str = getCurrentPopupString(hh)
%# getCurrentPopupString returns the currently selected string in the popupmenu with handle hh

%# could test input here
if ~ishandle(hh) || strcmp(get(hh,'Type'),'popupmenu')
error('getCurrentPopupString needs a handle to a popupmenu as input')
end

%# get the string - do it the readable way
list = get(hh,'String');
val = get(hh,'Value');
if iscell(list)
   str = list{val};
else
   str = list(val,:);
end

function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double


% --- Executes during object creation, after setting all properties.
function edit1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
set(handles.pushbutton1,'Enable','off');
set(handles.popupmenu2,'Visible','off');
    set(handles.text4,'Visible','off');
    set(handles.pushbutton2,'Visible','off');
    set(handles.text9,'Visible','off');
    set(handles.text5,'Visible','off');
    set(handles.text7,'Visible','off');
    set(handles.text5,'Visible','off');
    set(handles.text11,'Visible','off');
    set(handles.popupmenu1,'String',' ');
    set(handles.popupmenu1,'Visible','off');
sqlpass=num2str(handles.initial_parameter);
    javaaddpath('\myJavaClasses\mysql-connector-java-5.1.26-bin.jar')
%# connection parameteres
host = 'localhost';
user = 'root';
password =sqlpass;
dbName = 'library'; 
%# JDBC parameters
jdbcString = sprintf('jdbc:mysql://%s/%s', host, dbName);
jdbcDriver = 'com.mysql.jdbc.Driver';
isbn=get(handles.edit1,'String');
if(str2num(isbn)<=0)
    errordlg('Invalid Inputs Detected !')
    set(handles.edit1,'String','');
else
%# Create the database connection object
conn = database(dbName, user , password, jdbcDriver, jdbcString);
no='NO';

if isconnection(conn) % check to make sure that we successfully connected
    qry = sprintf('SELECT book_code,isbn,book_name,author_name,publisher_name,edition,price,issue,issued_to,issued_date,category from book WHERE isbn=''%s'' && issue=''%s''',isbn,no);
    rs = fetch(exec(conn, qry));
    rsdata = get(rs, 'Data');
    set(handles.uitable2,'Data',rsdata);
    if (strcmp(rsdata(1,1),'No Data')==1)
        set(handles.text7,'Visible','on');
        set(handles.text9,'Visible','off');
    set(handles.text5,'Visible','on');
    else
        set(handles.popupmenu1,'Visible','on');
        set(handles.text11,'Visible','on');
        set(handles.text4,'Visible','on');
        set(handles.popupmenu2,'Visible','on');
        set(handles.popupmenu1,'String',rsdata(:,1));
        set(handles.pushbutton2,'Visible','on');
        set(handles.text9,'Visible','on');
        set(handles.text5,'Visible','on');
    end
    zero='0';
    qry = sprintf('SELECT id from MEMBER where issue_status=''%s''',zero); 
    rs = fetch(exec(conn, qry));
    rsdata = get(rs, 'Data');
    set(handles.popupmenu2,'String',rsdata);
    
end
end
    
      
    
    



% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)






% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
sqlpass=num2str(handles.initial_parameter);
javaaddpath('\myJavaClasses\mysql-connector-java-5.1.26-bin.jar')
%# connection parameteres
host = 'localhost';
user = 'root';
password = sqlpass;
dbName = 'library'; 
%# JDBC parameters
jdbcString = sprintf('jdbc:mysql://%s/%s', host, dbName);
jdbcDriver = 'com.mysql.jdbc.Driver';
book_code=getCurrentPopupString(handles.popupmenu1);

student_id=getCurrentPopupString(handles.popupmenu2);
issue_date=get(handles.edit3,'String');

%# Create the database connection object
conn = database(dbName, user , password, jdbcDriver, jdbcString);


if isconnection(conn) % check to make sure that we successfully connected
    issue='YES';
    no='NO';
    
    qry = sprintf('UPDATE BOOK SET issued_to=''%s'',issued_date=''%s'',issue=''%s'' WHERE book_code=''%s''&& issue=''%s'';',student_id,issue_date,issue,book_code,no);
    
one='1';
     exec(conn, qry)
     qry1 = sprintf('UPDATE MEMBER SET issue_status=''%s'',BOOK1=''%s''where id=''%s''',one,book_code,student_id);
     exec(conn, qry1)
     msgbox('Issued Successfully !');
     set(handles.pushbutton2,'Enable','off');
     set(handles.popupmenu2,'String','');

end
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)



function edit3_Callback(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit3 as text
%        str2double(get(hObject,'String')) returns contents of edit3 as a double


% --- Executes during object creation, after setting all properties.
function edit3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in checkbox1.
function checkbox1_Callback(hObject, eventdata, handles)
if (get(handles.checkbox1,'Value') == get(handles.checkbox1,'Max'))
 % Checkbox is checked-take approriate action
 set(handles.edit3,'Enable','on')
else
    set(handles.edit3,'Enable','off')
end
 % Checkbox is not checked-take approriate action

% hObject    handle to checkbox1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of checkbox1


% --- Executes during object creation, after setting all properties.
function pushbutton1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called



function edit4_Callback(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit4 as text
%        str2double(get(hObject,'String')) returns contents of edit4 as a double


% --- Executes during object creation, after setting all properties.
function edit4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit5_Callback(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit5 as text
%        str2double(get(hObject,'String')) returns contents of edit5 as a double


% --- Executes during object creation, after setting all properties.
function edit5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on selection change in popupmenu1.
function popupmenu1_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns popupmenu1 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu1


% --- Executes during object creation, after setting all properties.
function popupmenu1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to popupmenu1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on selection change in listbox1.
function listbox1_Callback(hObject, eventdata, handles)
% hObject    handle to listbox1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns listbox1 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from listbox1


% --- Executes during object creation, after setting all properties.
function listbox1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to listbox1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
set(handles.pushbutton1,'Enable','on');
set(handles.edit1,'String','');
set(handles.text5,'Visible','off');
set(handles.text9,'Visible','off');
set(handles.text4,'Visible','off');
set(handles.popupmenu2,'Visible','off');
set(handles.text7,'Visible','off');
set(handles.popupmenu1,'Visible','off');
set(handles.text11,'Visible','off');
set(handles.pushbutton2,'Visible','off');
set(handles.uitable2,'Data','');
set(handles.pushbutton2,'Enable','on');

% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on selection change in popupmenu2.
function popupmenu2_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns popupmenu2 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu2


% --- Executes during object creation, after setting all properties.
function popupmenu2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to popupmenu2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


