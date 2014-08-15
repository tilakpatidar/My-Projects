function varargout = delete_member(varargin)
% DELETE_MEMBER M-file for delete_member.fig
%      DELETE_MEMBER, by itself, creates a new DELETE_MEMBER or raises the existing
%      singleton*.
%
%      H = DELETE_MEMBER returns the handle to a new DELETE_MEMBER or the handle to
%      the existing singleton*.
%
%      DELETE_MEMBER('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in DELETE_MEMBER.M with the given input arguments.
%
%      DELETE_MEMBER('Property','Value',...) creates a new DELETE_MEMBER or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before delete_member_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to delete_member_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help delete_member

% Last Modified by GUIDE v2.5 26-Oct-2013 21:54:58

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @delete_member_OpeningFcn, ...
                   'gui_OutputFcn',  @delete_member_OutputFcn, ...
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


% --- Executes just before delete_member is made visible.
function delete_member_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to delete_member (see VARARGIN)

% Choose default command line output for delete_member
handles.output = hObject;
handles.initial_parameter=varargin{1};
sqlpass=handles.initial_parameter;
% Update handles structure
guidata(hObject, handles);

% UIWAIT makes delete_member wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = delete_member_OutputFcn(hObject, eventdata, handles) 
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


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
answer=questdlg('Confirm Delete ?','Delete Member','Yes','No','Yes');
drawnow;
pause (0.05);
switch answer
    case 'Yes'
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

%# Create the database connection object
conn = database(dbName, user , password, jdbcDriver, jdbcString);
id=get(handles.edit1,'String');

if isconnection(conn) % check to make sure that we successfully connected
    qry = sprintf('DELETE from MEMBER where id=''%s''',id);
    exec(conn, qry);
    set(handles.edit1,'String','');
    msgbox('Successfully Deleted !');
end
    case'No'
        close delete_member;
end;
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


