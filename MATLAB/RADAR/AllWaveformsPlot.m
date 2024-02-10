% This program will generate a graph of a "chirp sweep"
% mayby I can get it to encode mesages as well, that would be cool.
% The program needs the input of ranges, in Hz, slope, and divisions.
clear
close all
clc
%----------Step Parameters----------%
firstStep = 76;            
secondStep = 77;
thirdStep =78;
fourthStep = 79;
fifthStep = 80;    
divisionsHz = 5;      % Total number of Steps

%----------Slope Parameters----------%
firstSlope = .25;        
secondSlope = .5;
thirdSlope = 1;       
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
    MMFSK = [p3y p2y];
    p1x = p3x;

   % plot(xup, yup, 'k', LineWidth=2)
    %plot(xdown, MMFSK, 'k', LineWidth=2)
    title('MFSK Waveform')
    grid("on")
    xlabel('Time in (ms)')
    ylabel("Frequency in (GHz)")
    end
    end

%-----FMCW Plot-----%
FMCWx = [0,35];
FMCW = [76,81];
%plot(FMCWx,FMCW, 'b', LineWidth=2)
FMCWx1 = [35,70];
FMCW1 = [81,76];
%plot(FMCWx1,FMCW1, 'b', LineWidth=2)

%-----MFSK Plot---
%-----BMFSK Plot-----%
BMFSK1x = [42,56];
BMFSK= [76,76];
%plot(BMFSK1x, BMFSK, 'm', LineWidth=2)
BMFSK2x =[28,42]; 
BMFSK2y = [77,77];
%plot(BMFSK2x, BMFSK2y, 'm', LineWidth=2)
BMFSK3x = [14,28];
BMFSK3y = [78,78];
%plot(BMFSK3x, BMFSK3y, 'm', LineWidth=2)
BMFSK4x = [56,70]; 
BMFSK4y = [79,79];
%plot(BMFSK4x, BMFSK4y, 'm', LineWidth=2)
BMFSK5x = [0,14];
BMFSK5y = [80,80];
%plot(BMFSK5x, BMFSK5y, 'm', LineWidth=2)

MFSK1x = [0,14];
MFSK= [76,76];
plot(MFSK1x, MFSK, 'g', LineWidth=2)
MFSK2x = [14,28];
MFSK2y = [77,77];
plot(MFSK2x, MFSK2y, 'g', LineWidth=2)
MFSK3x = [28,42]; 
MFSK3y = [78,78];
plot(MFSK3x, MFSK3y, 'g', LineWidth=2)
MFSK4x = [42,56];
MFSK4y = [79,79];
plot(MFSK4x, MFSK4y, 'g', LineWidth=2)
MFSK5x = [56,70];
MFSK5y = [80,80];
plot(MFSK5x, MFSK5y, 'g', LineWidth=2)
