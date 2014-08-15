function varargout = control_panel(varargin)
% CONTROL_PANEL M-file for control_panel.fig
%      CONTROL_PANEL, by itself, creates a new CONTROL_PANEL or raises the existing
%      singleton*.
%
%      H = CONTROL_PANEL returns the handle to a new CONTROL_PANEL or the handle to
%      the existing singleton*.
%
%      CONTROL_PANEL('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in CONTROL_PANEL.M with the given input arguments.
%
%      CONTROL_PANEL('Property','Value',...) creates a new CONTROL_PANEL or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before control_panel_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to control_panel_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help control_panel

% Last Modified by GUIDE v2.5 15-Oct-2013 20:53:29

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @control_panel_OpeningFcn, ...
                   'gui_OutputFcn',  @control_panel_OutputFcn, ...
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


% --- Executes just before control_panel is made visible.
function control_panel_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to control_panel (see VARARGIN)

% Choose default command line output for control_panel
handles.output = hObject;
handles.initial_parameter=varargin{1};

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes control_panel wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = control_panel_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
sqlpass=num2str(handles.initial_parameter);
mysql_password_utility(sqlpass)
close control_panel
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
sqlpass=num2str(handles.initial_parameter);
software_password(sqlpass)

close control_panel
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


