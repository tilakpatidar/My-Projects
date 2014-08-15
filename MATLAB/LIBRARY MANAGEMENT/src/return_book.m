function varargout = return_book(varargin)
% RETURN_BOOK M-file for return_book.fig
%      RETURN_BOOK, by itself, creates a new RETURN_BOOK or raises the existing
%      singleton*.
%
%      H = RETURN_BOOK returns the handle to a new RETURN_BOOK or the
%      handle to
%      the existing singleton*.
%
%      RETURN_BOOK('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in RETURN_BOOK.M with the given input arguments.
%
%      RETURN_BOOK('Property','Value',...) creates a new RETURN_BOOK or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before return_book_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to return_book_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help return_book

% Last Modified by GUIDE v2.5 26-Oct-2013 20:14:17

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @return_book_OpeningFcn, ...
                   'gui_OutputFcn',  @return_book_OutputFcn, ...
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


% --- Executes just before return_book is made visible.
function return_book_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to return_book (see VARARGIN)

% Choose default command line output for return_book
handles.output = hObject;
handles.initial_parameter=varargin{1};
sqlpass=handles.initial_parameter;
% Update handles structure
guidata(hObject, handles);

% UIWAIT makes return_book wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = return_book_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
tdate=date;
tdate=datestr(tdate,31);
set(handles.edit2,'String',tdate);
% Get default command line output from handles structure
varargout{1} = handles.output;




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
td=get(handles.edit2,'String');
book_code=get(handles.edit1,'String');
pd=datenum(td);
sqlpass=num2str(handles.initial_parameter);
%# add path to the JAR file you just installed to Java dynamic classpath
javaaddpath('\myJavaClasses\mysql-connector-java-5.1.26-bin.jar')
%# connection parameteres
host = 'localhost';
user = 'root';
password = sqlpass;
dbName = 'library'; 
%# JDBC parameters
jdbcString = sprintf('jdbc:mysql://%s/%s', host, dbName);
jdbcDriver = 'com.mysql.jdbc.Driver';

%# Create the database connection object
conn = database(dbName, user , password, jdbcDriver, jdbcString);


if isconnection(conn) % check to make sure that we successfully connected
    qry = sprintf('SELECT issued_date from book where book_code=''%s'' && issue=''%s''',book_code,'YES');
    rs = fetch(exec(conn, qry));
    rsdata = get(rs, 'Data');
end
    if(strcmp(rsdata,'No Data')==1)
    msgbox('Invalid Input or book not issued !');
    set(handles.edit3,'String','');
    set(handles.edit1,'String','');
    set(handles.edit7,'String','');
else
    set(handles.edit3,'String',rsdata);
    a=datenum(get(handles.edit3,'String'));
    rd=addtodate(a,15,'day');
    


    
if(datenum(pd)<=datenum(rd))
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

%# Create the database connection object
conn = database(dbName, user , password, jdbcDriver, jdbcString);


no='NO';
yes='YES';


book_code=get(handles.edit1,'String');

if(isconnection(conn))
    qry = sprintf('UPDATE book SET issued_date=DEFAULT,issue=''%s'',issued_to=DEFAULT where book_code=''%s'' && issue=''%s''',no,book_code,yes);
   exec(conn, qry);   
    
   zero='0';
   book_code='0';
   student_id=get(handles.edit7,'String');
 qry1 = sprintf('UPDATE MEMBER SET issue_status=''%s'',BOOK1=''%s'' where id=''%s'';',zero,book_code,student_id);
     exec(conn, qry1);
msgbox('Book returned Successfully !')
end
else
    set(handles.uipanel1,'Visible','on');
    t=daysact(rd,pd);
  
    set(handles.edit4,'String',t);
    
end
    end


% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)



function edit2_Callback(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit2 as text
%        str2double(get(hObject,'String')) returns contents of edit2 as a double


% --- Executes during object creation, after setting all properties.
function edit2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
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
 set(handles.edit2,'Enable','on')
else
    set(handles.edit2,'Enable','off')
end


% hObject    handle to checkbox1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of checkbox1



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



function edit6_Callback(hObject, eventdata, handles)
% hObject    handle to edit6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit6 as text
%        str2double(get(hObject,'String')) returns contents of edit6 as a double


% --- Executes during object creation, after setting all properties.
function edit6_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
  rate=STR2DOUBLE(get(handles.edit5,'String'));
  t=str2DOUBLE(get(handles.edit4,'String'));
  fine=t*rate;
  set(handles.edit6,'String',fine);
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
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

%# Create the database connection object
conn = database(dbName, user , password, jdbcDriver, jdbcString);


no='NO';
yes='YES';


book_code=get(handles.edit1,'String');


    qry = sprintf('UPDATE book SET issued_date=DEFAULT,issue=''%s'',issued_to=DEFAULT where book_code=''%s'' && issue=''%s''',no,book_code,yes);
   exec(conn, qry);
   zero='0';
   book_code='0';
   student_id=get(handles.edit7,'String');
   qry1 = sprintf('UPDATE MEMBER SET issue_status=''%s'',BOOK1=''%s''where id=''%s''',zero,book_code,student_id);
     exec(conn, qry1)
   msgbox('Successfully paid and returned !');
   set(handles.uipanel1,'Visible','off');
   set(handles.edit6,'String','');
   set(handles.edit4,'String','');
   set(handles.edit5,'String','');
   set(handles.edit1,'String','');
   set(handles.edit7,'String','');
   
   
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)



function edit7_Callback(hObject, eventdata, handles)
% hObject    handle to edit7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit7 as text
%        str2double(get(hObject,'String')) returns contents of edit7 as a double


% --- Executes during object creation, after setting all properties.
function edit7_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


