package example.vego.com

import android.content.Context
import android.graphics.ColorSpace
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import android.widget.ImageView
import android.widget.TextView
import androidx.fragment.app.Fragment

class RecomAdapter (var mCtx: Context, var resources:Int, var items:List<Recommendation>):ArrayAdapter<Recommendation>(mCtx, resources, items) {

    override fun getView(position: Int, convertView: View?, parent: ViewGroup): View {
        val layoutInflater:LayoutInflater = LayoutInflater.from(mCtx)
        val view:View = layoutInflater.inflate(resources, null)

        val imageView:ImageView = view.findViewById(R.id.image)
        val titleTextView: TextView = view.findViewById(R.id.textView)
        val descriptionTextView: TextView = view.findViewById(R.id.textView2)

        var mItem:Recommendation = items[position]
        imageView.setImageDrawable(mCtx.resources.getDrawable(mItem.img))
        titleTextView.text = mItem.title
        descriptionTextView.text = mItem.description



        return view
    }

}