% This program will generate a graph of a "chirp sweep"
% mayby I can get it to encode mesages as well, that would be cool.
% The program needs the input of ranges, in Hz, slope, and divisions.
clear
close all
clc
%----------Step Parameters----------%
firstStep = 80;            
secondStep = 76;
thirdStep =79;
fourthStep = 77;
fifthStep = 78;    
divisionsHz = 5;      % Total number of Steps

%----------Slope Parameters----------%
firstSlope = .5;        
secondSlope = 1;
thirdSlope = .25;       
divisionsSlope = 3;   % Total number of Slopes

% This divides the sweep into the desired number of points
% NOTE: it starts at the first and ends on the last
delY = [firstStep,secondStep,thirdStep,fourthStep,fifthStep];
Slope = [firstSlope,secondSlope,thirdSlope];
n = divisionsHz;

% Inittaliize
p1x = 0;
deltaY = 1;

% This is a single Chirp block
% need the up and the down, three points, each with x and y cordinats
% the graph is frequency with respect to time. the first point will be
% (0, y1) and the last will be (sumX, ylast)
   
    for ct = 1:n
        
     for mct = 1:divisionsSlope
        m = Slope(mct);
    hold on

    % Here are the equations for the three points that make up the chirp
    p1y = delY(ct);
    p2y = p1y + deltaY;
    p3y = p1y;

    p2x = (p2y-p1y)/m +  p1x;
    width = 2*(p2x-p1x);
    p3x = p1x + width;

    xup = [p1x p2x];
    yup = [p1y p2y];
    xdown = [p3x p2x];
    ydown = [p3y p2y];
    p1x = p3x;

    plot(xup, yup, 'r', LineWidth=1)
    plot(xdown, ydown, 'r', LineWidth=1)
    title('Frequency Modulation')
    grid("on")
    xlabel('Time in (ms)')
    ylabel("Frequency in (GHz)")
    end
   end
