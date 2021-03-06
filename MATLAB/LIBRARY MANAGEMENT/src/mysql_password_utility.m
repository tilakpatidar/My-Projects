function varargout = mysql_password_utility(varargin)
% MYSQL_PASSWORD_UTILITY M-file for mysql_password_utility.fig
%      MYSQL_PASSWORD_UTILITY, by itself, creates a new MYSQL_PASSWORD_UTILITY or raises the existing
%      singleton*.
%
%      H = MYSQL_PASSWORD_UTILITY returns the handle to a new MYSQL_PASSWORD_UTILITY or the handle to
%      the existing singleton*.
%
%      MYSQL_PASSWORD_UTILITY('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in MYSQL_PASSWORD_UTILITY.M with the given input arguments.
%
%      MYSQL_PASSWORD_UTILITY('Property','Value',...) creates a new MYSQL_PASSWORD_UTILITY or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before mysql_password_utility_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to mysql_password_utility_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help mysql_password_utility

% Last Modified by GUIDE v2.5 16-Oct-2013 18:18:50

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @mysql_password_utility_OpeningFcn, ...
                   'gui_OutputFcn',  @mysql_password_utility_OutputFcn, ...
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


% --- Executes just before mysql_password_utility is made visible.
function mysql_password_utility_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to mysql_password_utility (see VARARGIN)

% Choose default command line output for mysql_password_utility
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes mysql_password_utility wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = mysql_password_utility_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

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
currentpass=csql_passwordUI();
newpass=nsql_passwordUI();
query=sprintf('SET PASSWORD=PASSWORD(''%s'')',newpass);

javaaddpath('\myJavaClasses\mysql-connector-java-5.1.26-bin.jar')
%# connection parameteres
host = 'localhost';
user = 'root';
password = currentpass;
dbName = 'library'; 
%# JDBC parameters
jdbcString = sprintf('jdbc:mysql://%s/%s', host, dbName);
jdbcDriver = 'com.mysql.jdbc.Driver';

%# Create the database connection object
conn = database(dbName, user , password, jdbcDriver, jdbcString);
if isconnection(conn)
    button = questdlg('Changing MySQL password requires a restart. Are you sure you want to continue?','Confirm Restart','Yes','No','Yes'); %default option is yes
   drawnow; pause(0.05); 
   switch button
   case 'Yes'
               
            exec(conn, query);
close start;
LOGIN;
close this;



     
    case 'No'
        currentpass='';
            newpass='';
        otherwise
            currentpass='';
            newpass='';
   end;

else
    msgbox('Invalid Current MySQL password !');
    currentpass='';
            newpass='';
end;
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
set(handles.edit1,'String','');
set(handles.edit2,'String','');
set(handles.pushbutton1,'Enable','on');
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


