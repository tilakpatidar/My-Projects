function varargout = book_search(varargin)


% BOOK_SEARCH M-file for book_search.fig
%      BOOK_SEARCH, by itself, creates a new BOOK_SEARCH or raises the existing
%      singleton*.
%
%      H = BOOK_SEARCH returns the handle to a new BOOK_SEARCH or the handle to
%      the existing singleton*.
%
%      BOOK_SEARCH('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in BOOK_SEARCH.M with the given input arguments.
%
%      BOOK_SEARCH('Property','Value',...) creates a new BOOK_SEARCH or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before book_search_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to book_search_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help book_search

% Last Modified by GUIDE v2.5 15-Oct-2013 21:41:21

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @book_search_OpeningFcn, ...
                   'gui_OutputFcn',  @book_search_OutputFcn, ...
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


% --- Executes just before book_search is made visible.
function book_search_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to book_search (see VARARGIN)

% Choose default command line output for book_search
handles.output = hObject;
handles.initial_parameter=varargin{1};
sqlpass=num2str(handles.initial_parameter);
% Update handles structure
guidata(hObject, handles);


% UIWAIT makes book_search wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = book_search_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;
imshow('search.jpg',handles.axes1);
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

% --- Executes during object creation, after setting all properties.
function edit3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
clear=[];
set(handles.edit1,'String','');
set(handles.uitable1,'Data',clear);



% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
if (get(handles.radiobutton1,'Value') == get(handles.radiobutton1,'Max'))
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
book_name=get(handles.edit1,'String');

%# Create the database connection object
conn = database(dbName, user , password, jdbcDriver, jdbcString);


if isconnection(conn) % check to make sure that we successfully connected
    qry = sprintf('SELECT * from book WHERE book_name LIKE ''%s''',strcat(strcat('%',book_name),'%'));
    rs = fetch(exec(conn, qry));
    rsdata = get(rs, 'Data');
    set(handles.uitable1,'Data',rsdata);
end;
end;
 if (get(handles.radiobutton2,'Value') == get(handles.radiobutton2,'Max'))
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
author_name=get(handles.edit1,'String');

%# Create the database connection object
conn = database(dbName, user , password, jdbcDriver, jdbcString);


if isconnection(conn) % check to make sure that we successfully connected
    qry = sprintf('SELECT * from book WHERE author_name LIKE ''%s''',strcat(strcat('%',author_name),'%'));
    rs = fetch(exec(conn, qry));
    rsdata = get(rs, 'Data');
    set(handles.uitable1,'Data',rsdata);
end
 end
if (get(handles.radiobutton3,'Value') == get(handles.radiobutton3,'Max'))
    sqlpass=num2str(handles.initial_parameter);
 %# add path to the JAR file you just installed to Java dynamic classpath
javaaddpath('\myJavaClasses\mysql-connector-java-5.1.26-bin.jar')
%# connection parameteres
host = 'localhost';
user = 'root';
password = sqlpass;
dbName = 'library'; 
%# JDBC parametersra
jdbcString = sprintf('jdbc:mysql://%s/%s', host, dbName);
jdbcDriver = 'com.mysql.jdbc.Driver';
publisher_name=get(handles.edit1,'String');

%# Create the database connection object
conn = database(dbName, user , password, jdbcDriver, jdbcString);


if isconnection(conn) % check to make sure that we successfully connected
    qry = sprintf('SELECT * from book WHERE publisher_name LIKE ''%s''',strcat(strcat('%',publisher_name),'%'));
    rs = fetch(exec(conn, qry));
    rsdata = get(rs, 'Data');
    set(handles.uitable1,'Data',rsdata);
end
end
if (get(handles.radiobutton6,'Value') == get(handles.radiobutton6,'Max'))
    sqlpass=num2str(handles.initial_parameter);
 %# add path to the JAR file you just installed to Java dynamic classpath
javaaddpath('\myJavaClasses\mysql-connector-java-5.1.26-bin.jar')
%# connection parameteres
host = 'localhost';
user = 'root';
password = sqlpass;
dbName = 'library'; 
%# JDBC parametersra
jdbcString = sprintf('jdbc:mysql://%s/%s', host, dbName);
jdbcDriver = 'com.mysql.jdbc.Driver';


%# Create the database connection object
conn = database(dbName, user , password, jdbcDriver, jdbcString);
category=getCurrentPopupString(handles.popupmenu2);

if isconnection(conn) % check to make sure that we successfully connected
    qry = sprintf('SELECT * from book WHERE category=''%s''',category);
    rs = fetch(exec(conn, qry));
    rsdata = get(rs, 'Data');
    set(handles.uitable1,'Data',rsdata);
end
end




% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in radiobutton1.
function radiobutton1_Callback(hObject, eventdata, handles)
set(handles.popupmenu2,'Visible','off');
set(handles.edit1,'Visible','on');
% hObject    handle to radiobutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton1


% --- Executes on button press in radiobutton2.
function radiobutton2_Callback(hObject, eventdata, handles)
set(handles.popupmenu2,'Visible','off');
set(handles.edit1,'Visible','on');

% hObject    handle to radiobutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton2


% --- Executes on button press in radiobutton3.
function radiobutton3_Callback(hObject, eventdata, handles)
set(handles.popupmenu2,'Visible','off');
set(handles.edit1,'Visible','on');
% hObject    handle to radiobutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton3



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


% --- Executes on button press in radiobutton6.
function radiobutton6_Callback(hObject, eventdata, handles)
if (get(handles.radiobutton6,'Value') == get(handles.radiobutton6,'Max'))
    set(handles.popupmenu2,'Visible','on');
    set(handles.edit1,'Visible','off');
else
    set(handles.popupmenu2,'Visible','off');
    set(handles.edit1,'Visible','on');
end
    


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


