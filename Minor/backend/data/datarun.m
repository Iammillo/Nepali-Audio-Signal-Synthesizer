for i=1:375
  A = sprintf('%d.wav',i);
  [data,fs]= audioread(A);
  plot(data);
  input(' ');
 end