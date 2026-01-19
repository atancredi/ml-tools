import torch

def validate_model(model, val_loader, criterion):
    model.eval()
    running_val_loss = 0.0
    
    with torch.no_grad(): # No gradient needed for validation
        for inputs, targets in val_loader:
            inputs = inputs.view(inputs.size(0), -1)
            targets = targets.view(targets.size(0), -1)
            
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            running_val_loss += loss.item()
            
    avg_val_loss = running_val_loss / len(val_loader)
    return avg_val_loss