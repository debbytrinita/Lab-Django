from wishlist.models import BarangWishlist
from django import forms
class wishlist_form(forms.ModelForm):
    class Meta:
        model = BarangWishlist
        fields =('nama_barang', 'harga_barang','deskripsi')

        widgets = {
            'nama_barang': forms.TextInput(attrs={'class':'form-control', 'placeholder':'masukkan judul'}),
            'harga_barang': forms.TextInput(attrs={'class':'form-control', 'placeholder':'masukkan deskripsi'}),
            'deskripsi': forms.TextInput(attrs={'class':'form-control', 'placeholder':'masukkan judul'}),
        }