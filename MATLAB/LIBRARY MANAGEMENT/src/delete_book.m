function varargout = delete_book(varargin)
% DELETE_BOOK M-file for delete_book.fig
%      DELETE_BOOK, by itself, creates a new DELETE_BOOK or raises the existing
%      singleton*.
%
%      H = DELETE_BOOK returns the handle to a new DELETE_BOOK or the handle to
%      the existing singleton*.
%
%      DELETE_BOOK('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in DELETE_BOOK.M with the given input arguments.
%
%      DELETE_BOOK('Property','Value',...) creates a new DELETE_BOOK or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before delete_book_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to delete_book_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help delete_book

% Last Modified by GUIDE v2.5 15-Oct-2013 13:19:53

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @delete_book_OpeningFcn, ...
                   'gui_OutputFcn',  @delete_book_OutputFcn, ...
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


% --- Executes just before delete_book is made visible.
function delete_book_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to delete_book (see VARARGIN)

% Choose default command line output for delete_book
handles.output = hObject;
handles.initial_parameter=varargin{1};
sqlpass=handles.initial_parameter;
% Update handles structure
guidata(hObject, handles);

% UIWAIT makes delete_book wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = delete_book_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;
imshow('remove.jpg',handles.axes1);

% --- Executes on button press in checkbox1.
function checkbox1_Callback(hObject, eventdata, handles)

% hObject    handle to checkbox1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of checkbox1


% --- Executes on button press in checkbox2.
function checkbox2_Callback(hObject, eventdata, handles)

% hObject    handle to checkbox2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of checkbox2



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


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
if (get(handles.radiobutton1,'Value') == get(handles.radiobutton1,'Max'))
sqlpass=num2str(handles.initial_parameter);
    % Radio button is selected-take approriate action
 javaaddpath('\myJavaClasses\mysql-connector-java-5.1.26-bin.jar')
%# connection parameteres
host = 'localhost';
user = 'root';
password = sqlpass;
dbName = 'library'; 
%# JDBC parameters
jdbcString = sprintf('jdbc:mysql://%s/%s', host, dbName);
jdbcDriver = 'com.mysql.jdbc.Driver';
isbn=get(handles.edit1,'String');

%# Create the database connection object
conn = database(dbName, user , password, jdbcDriver, jdbcString);
        
            if isconnection(conn) % check to make sure that we successfully connected
           qry= sprintf('SELECT book_code FROM book WHERE isbn=''%s'';',isbn);  
           rs=fetch(exec(conn, qry));
           rsdata = get(rs, 'Data');
           if(strcmp(rsdata,'No Data')==1)
               errordlg('Invalid ISBN code or Invalid Input !');
               set(handles.edit1,'String','');
           else
               
    qry1 = sprintf('DELETE FROM book WHERE isbn=''%s'';',isbn);
    exec(conn,qry1)
    msgbox('Successfully Deleted !')
    set(handles.edit1,'String','');
    set(handles.edit2,'String','');
           end
           end
    
           end

if(get(handles.radiobutton2,'Value') == get(handles.radiobutton2,'Max'))
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

book_code=get(handles.edit2,'String');



%# Create the database connection object
conn = database(dbName, user , password, jdbcDriver, jdbcString);
        
if isconnection(conn) % check to make sure that we successfully connected
           qry= sprintf('SELECT isbn FROM book WHERE book_code=''%s'';',book_code);  
           rs=fetch(exec(conn, qry));
           rsdata = get(rs, 'Data');
           if(strcmp(rsdata,'No Data')==1)
               msgbox('Invalid BOOK code or Invalid Input!');
               set(handles.edit2,'String','');
           else
               
    qry1 = sprintf('DELETE FROM book WHERE book_code=''%s'';',book_code);
    exec(conn,qry1)
    msgbox('Successfully Deleted !')
    set(handles.edit1,'String','');
            set(handles.edit2,'String','');
           end
end
            
            
end        
 % Radio button is not selected-take approriate action

% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
set(handles.edit1,'String','');
set(handles.edit2,'String','');

% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in radiobutton1.
function radiobutton1_Callback(hObject, eventdata, handles)
set(handles.edit1,'String','');
set(handles.edit2,'String','');
set(handles.edit1,'Enable','on');
set(handles.edit2,'Enable','off');
% hObject    handle to radiobutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton1


% --- Executes on button press in radiobutton2.
function radiobutton2_Callback(hObject, eventdata, handles)
set(handles.edit2,'String','');
set(handles.edit1,'String','');
set(handles.edit1,'Enable','off');
set(handles.edit2,'Enable','on');
% hObject    handle to radiobutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton2


