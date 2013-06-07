function [all_theta] = oneVsAll(X, y, num_labels, lambda)
% ONEVSALL trains multiple logistic regression classifiers and returns all
% the classifiers in a matrix all_theta, where the i-th row of all_theta 
% corresponds to the classifier for label i

m = size(X, 1);
n = size(X, 2);

all_theta = zeros(num_labels, n + 1);

% Add ones to the X data matrix
X = [ones(m, 1) X];

% Set Initial theta
initial_theta = zeros(n + 1, 1);
% Set options for fminunc
options = optimset('GradObj', 'on', 'MaxIter', 50); 

for c = 1:num_labels
	% Run fmincg to obtain the optimal theta
	% This function will return theta and the cost 
	theta = fmincg (@(t)(lrCostFunction(t, X, (y == c), lambda)), initial_theta, options);
	all_theta(c,:) = theta;
end

end
