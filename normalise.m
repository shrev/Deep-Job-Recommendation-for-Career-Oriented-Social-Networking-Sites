function[values] = normalise(x,mean,variance)

sd = sqrt(variance);

w = zeros(size(x));

sd = norm(sd);

w = mean + randn(size(w,1),size(w,2)).*sd;

values = w;

end