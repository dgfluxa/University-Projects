package example.vego.com

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import android.widget.ImageView
import android.widget.TextView

class SetAdapter(var mCtx: Context, var resources:Int, var items:List<Setting>):
    ArrayAdapter<Setting>(mCtx, resources, items) {

    override fun getView(position: Int, convertView: View?, parent: ViewGroup): View {
        val layoutInflater: LayoutInflater = LayoutInflater.from(mCtx)
        val view: View = layoutInflater.inflate(resources, null)

        val titleTextView: TextView = view.findViewById(R.id.textView)

        var mItem:Setting = items[position]

        titleTextView.text = mItem.title



        return view
    }

}